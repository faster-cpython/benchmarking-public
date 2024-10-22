# Results vs. 3.13.0

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.01x faster
- HPT reliability: 99.46%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 240 ms: 1.11x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.85 sec: 1.18x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 96.1 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 550 ms: 1.19x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.39 sec: 1.18x faster                                                     |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_none            | 223 ms                                                      | 215 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 547 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 50.0 ms: 1.29x faster                                                      |
| float          | 48.1 ms                                                     | 44.3 ms: 1.09x faster                                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| regex_v8       | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                      |
| regex_dna      | 114 ms                                                      | 124 ms: 1.09x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 90.0 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| xml_etree_generate   | 53.3 ms                                                     | 52.9 ms: 1.01x faster                                                      |
| json_loads           | 14.3 us                                                     | 14.4 us: 1.01x slower                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 5.94 ms: 1.03x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.0 ms: 1.04x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 134 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.08 ms: 1.23x faster                                                      |
| django_template | 21.8 ms                                                     | 25.1 ms: 1.15x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 38.6 ms: 1.18x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.5 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 515 us: 16.85x faster                                                      |
| deepcopy_memo              | 21.8 us                                                     | 16.3 us: 1.34x faster                                                      |
| nbody                      | 64.5 ms                                                     | 50.0 ms: 1.29x faster                                                      |
| spectral_norm              | 59.2 ms                                                     | 46.7 ms: 1.27x faster                                                      |
| mako                       | 6.24 ms                                                     | 5.08 ms: 1.23x faster                                                      |
| deepcopy                   | 223 us                                                      | 184 us: 1.22x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 550 ms: 1.19x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.39 sec: 1.18x faster                                                     |
| scimark_sor                | 72.0 ms                                                     | 61.5 ms: 1.17x faster                                                      |
| scimark_fft                | 174 ms                                                      | 149 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                       |
| fannkuch                   | 245 ms                                                      | 217 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| pyflate                    | 275 ms                                                      | 248 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.13 ms: 1.10x faster                                                      |
| float                      | 48.1 ms                                                     | 44.3 ms: 1.09x faster                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 40.0 ms: 1.07x faster                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.27 sec: 1.07x faster                                                     |
| scimark_monte_carlo        | 40.3 ms                                                     | 37.7 ms: 1.07x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.59 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_none            | 223 ms                                                      | 215 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 493 ms                                                      | 475 ms: 1.04x faster                                                       |
| pprint_pformat             | 991 ms                                                      | 975 ms: 1.02x faster                                                       |
| meteor_contest             | 72.3 ms                                                     | 71.7 ms: 1.01x faster                                                      |
| xml_etree_generate         | 53.3 ms                                                     | 52.9 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.4 us: 1.01x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 381 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.2 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.59 ms: 1.02x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 55.3 ms: 1.02x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 5.94 ms: 1.03x slower                                                      |
| python_startup_no_site     | 17.8 ms                                                     | 18.4 ms: 1.03x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 96.1 ms: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.0 ms: 1.04x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.44 sec: 1.04x slower                                                     |
| json                       | 2.98 ms                                                     | 3.13 ms: 1.05x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.01 us: 1.05x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.48 us: 1.05x slower                                                      |
| bench_mp_pool              | 69.6 ms                                                     | 73.4 ms: 1.05x slower                                                      |
| regex_v8                   | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 134 us: 1.06x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 42.9 ms: 1.06x slower                                                      |
| async_tree_io_tg           | 512 ms                                                      | 547 ms: 1.07x slower                                                       |
| regex_dna                  | 114 ms                                                      | 124 ms: 1.09x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 828 us: 1.09x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 42.0 ms: 1.09x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| 2to3                       | 217 ms                                                      | 240 ms: 1.11x slower                                                       |
| logging_silent             | 51.0 ns                                                     | 56.5 ns: 1.11x slower                                                      |
| nqueens                    | 55.5 ms                                                     | 61.6 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 191 ms: 1.12x slower                                                       |
| create_gc_cycles           | 829 us                                                      | 927 us: 1.12x slower                                                       |
| sqlglot_optimize           | 33.1 ms                                                     | 37.0 ms: 1.12x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.06 ms: 1.12x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 96.9 ms: 1.12x slower                                                      |
| pycparser                  | 758 ms                                                      | 851 ms: 1.12x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 90.0 ms: 1.12x slower                                                      |
| sympy_str                  | 166 ms                                                      | 188 ms: 1.13x slower                                                       |
| django_template            | 21.8 ms                                                     | 25.1 ms: 1.15x slower                                                      |
| sympy_expand               | 285 ms                                                      | 330 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 117 us: 1.16x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 38.6 ms: 1.18x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.85 sec: 1.18x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 17.5 ms: 1.18x slower                                                      |
| go                         | 84.6 ms                                                     | 100 ms: 1.19x slower                                                       |
| richards                   | 26.0 ms                                                     | 31.1 ms: 1.19x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.7 ms: 1.20x slower                                                      |
| richards_super             | 29.3 ms                                                     | 35.2 ms: 1.20x slower                                                      |
| pylint                     | 211 ms                                                      | 255 ms: 1.21x slower                                                       |
| raytrace                   | 156 ms                                                      | 194 ms: 1.24x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.34 ms: 1.26x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.75 ms: 1.29x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (8): async_tree_memoization, pickle_pure_python, xml_etree_iterparse, comprehensions, python_startup, coverage, pathlib, bench_thread_pool
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.46% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown