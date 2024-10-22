# Results vs. 3.13.0

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.78 sec: 1.13x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.4 ms: 1.10x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 535 ms: 1.22x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 248 ms: 1.16x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.55 sec: 1.06x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 398 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 550 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 588 ms: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 55.5 ms: 1.15x slower                                                      |
| nbody          | 64.5 ms                                                     | 84.9 ms: 1.32x slower                                                      |
| Geometric mean | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| regex_compile  | 80.1 ms                                                     | 92.3 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.4 ms: 1.02x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.34 ms: 1.10x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.0 ms: 1.11x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 69.7 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.7 ms: 1.14x slower                                                      |
| pickle_pure_python   | 183 us                                                      | 215 us: 1.17x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| unpickle_pure_python | 127 us                                                      | 153 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                                      |
| genshi_xml      | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                      |
| django_template | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 17.7 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 524 us: 16.56x faster                                                      |
| asyncio_tcp                | 654 ms                                                      | 535 ms: 1.22x faster                                                       |
| deepcopy                   | 223 us                                                      | 191 us: 1.17x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 248 ms: 1.16x faster                                                       |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.55 sec: 1.06x faster                                                     |
| async_tree_none_tg         | 206 ms                                                      | 198 ms: 1.04x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 21.1 us: 1.03x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.96 us: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| python_startup             | 22.2 ms                                                     | 21.9 ms: 1.01x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.3 us: 1.00x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.3 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 394 ms: 1.02x slower                                                       |
| tornado_http               | 92.8 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 95.4 ms: 1.02x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 88.9 ms: 1.03x slower                                                      |
| regex_dna                  | 114 ms                                                      | 118 ms: 1.03x slower                                                       |
| telco                      | 4.85 ms                                                     | 4.99 ms: 1.03x slower                                                      |
| sympy_expand               | 285 ms                                                      | 299 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 398 ms: 1.06x slower                                                       |
| sympy_str                  | 166 ms                                                      | 177 ms: 1.07x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 43.2 ms: 1.07x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 77.4 ms: 1.07x slower                                                      |
| 2to3                       | 217 ms                                                      | 233 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 550 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                      |
| pylint                     | 211 ms                                                      | 230 ms: 1.09x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                      |
| mako                       | 6.24 ms                                                     | 6.85 ms: 1.10x slower                                                      |
| html5lib                   | 38.6 ms                                                     | 42.4 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| json_dumps                 | 5.76 ms                                                     | 6.34 ms: 1.10x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.53 sec: 1.10x slower                                                     |
| xml_etree_generate         | 53.3 ms                                                     | 59.0 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 36.6 ms: 1.11x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 920 us: 1.11x slower                                                       |
| json                       | 2.98 ms                                                     | 3.32 ms: 1.11x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.37 us: 1.11x slower                                                      |
| genshi_xml                 | 32.8 ms                                                     | 36.6 ms: 1.12x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 69.7 ms: 1.12x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.88 us: 1.12x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.78 sec: 1.13x slower                                                     |
| async_tree_io              | 521 ms                                                      | 588 ms: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| django_template            | 21.8 ms                                                     | 24.8 ms: 1.14x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.7 ms: 1.14x slower                                                      |
| sqlglot_transpile          | 952 us                                                      | 1.09 ms: 1.15x slower                                                      |
| regex_compile              | 80.1 ms                                                     | 92.3 ms: 1.15x slower                                                      |
| sqlglot_parse              | 761 us                                                      | 878 us: 1.15x slower                                                       |
| float                      | 48.1 ms                                                     | 55.5 ms: 1.15x slower                                                      |
| sqlglot_normalize          | 171 ms                                                      | 198 ms: 1.16x slower                                                       |
| scimark_fft                | 174 ms                                                      | 203 ms: 1.16x slower                                                       |
| pprint_safe_repr           | 493 ms                                                      | 575 ms: 1.17x slower                                                       |
| chaos                      | 37.9 ms                                                     | 44.3 ms: 1.17x slower                                                      |
| pickle_pure_python         | 183 us                                                      | 215 us: 1.17x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 65.1 ms: 1.17x slower                                                      |
| typing_runtime_protocols   | 100 us                                                      | 118 us: 1.17x slower                                                       |
| pycparser                  | 758 ms                                                      | 892 ms: 1.18x slower                                                       |
| comprehensions             | 10.2 us                                                     | 12.1 us: 1.18x slower                                                      |
| pyflate                    | 275 ms                                                      | 325 ms: 1.18x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.18 sec: 1.19x slower                                                     |
| go                         | 84.6 ms                                                     | 101 ms: 1.19x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| genshi_text                | 14.9 ms                                                     | 17.7 ms: 1.19x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 64.7 ms: 1.20x slower                                                      |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.81 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 153 us: 1.20x slower                                                       |
| fannkuch                   | 245 ms                                                      | 297 ms: 1.21x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 52.1 ms: 1.22x slower                                                      |
| deltablue                  | 1.86 ms                                                     | 2.29 ms: 1.23x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 73.0 ms: 1.23x slower                                                      |
| scimark_monte_carlo        | 40.3 ms                                                     | 49.8 ms: 1.24x slower                                                      |
| raytrace                   | 156 ms                                                      | 193 ms: 1.24x slower                                                       |
| hexiom                     | 3.69 ms                                                     | 4.59 ms: 1.24x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 64.7 ns: 1.27x slower                                                      |
| richards                   | 26.0 ms                                                     | 33.7 ms: 1.29x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 93.1 ms: 1.29x slower                                                      |
| richards_super             | 29.3 ms                                                     | 37.9 ms: 1.29x slower                                                      |
| nbody                      | 64.5 ms                                                     | 84.9 ms: 1.32x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (7): async_tree_memoization, bench_thread_pool, async_tree_none, python_startup_no_site, bench_mp_pool, pathlib, regex_v8
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown