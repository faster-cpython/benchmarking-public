# Results vs. 3.13.0

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 232 ms: 1.07x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.79 sec: 1.13x slower                                                     |
| html5lib       | 38.6 ms                                                     | 42.3 ms: 1.10x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 95.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 397 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 398 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 561 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 599 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, asyncio_tcp, async_tree_memoization, async_tree_none, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 48.1 ms                                                     | 55.3 ms: 1.15x slower                                                      |
| nbody          | 64.5 ms                                                     | 91.2 ms: 1.42x slower                                                      |
| Geometric mean | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| regex_dna      | 114 ms                                                      | 125 ms: 1.09x slower                                                       |
| regex_v8       | 14.7 ms                                                     | 16.7 ms: 1.14x slower                                                      |
| regex_compile  | 80.1 ms                                                     | 94.2 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 14.1 us: 1.01x faster                                                      |
| xml_etree_parse      | 93.2 ms                                                     | 95.6 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.2 ms: 1.06x slower                                                      |
| json_dumps           | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.3 ms                                                     | 59.1 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 42.5 ms: 1.16x slower                                                      |
| unpickle_pure_python | 127 us                                                      | 152 us: 1.20x slower                                                       |
| tomli_loads          | 1.36 sec                                                    | 1.66 sec: 1.22x slower                                                     |
| pickle_pure_python   | 183 us                                                      | 226 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 36.9 ms: 1.13x slower                                                      |
| mako            | 6.24 ms                                                     | 7.13 ms: 1.14x slower                                                      |
| django_template | 21.8 ms                                                     | 26.2 ms: 1.21x slower                                                      |
| genshi_text     | 14.9 ms                                                     | 18.0 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.17x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 526 us: 16.49x faster                                                      |
| deepcopy                   | 223 us                                                      | 193 us: 1.15x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 255 ms: 1.13x faster                                                       |
| deepcopy_memo              | 21.8 us                                                     | 21.3 us: 1.03x faster                                                      |
| json_loads                 | 14.3 us                                                     | 14.1 us: 1.01x faster                                                      |
| python_startup             | 22.2 ms                                                     | 22.0 ms: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                     | 1.57 ms: 1.01x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.63 ms: 1.01x slower                                                      |
| coverage                   | 46.7 ms                                                     | 47.6 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 397 ms: 1.02x slower                                                       |
| telco                      | 4.85 ms                                                     | 4.97 ms: 1.03x slower                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 95.6 ms: 1.03x slower                                                      |
| tornado_http               | 92.8 ms                                                     | 95.3 ms: 1.03x slower                                                      |
| json                       | 2.98 ms                                                     | 3.07 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 398 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.2 ms: 1.06x slower                                                      |
| 2to3                       | 217 ms                                                      | 232 ms: 1.07x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.08x slower                                                      |
| meteor_contest             | 72.3 ms                                                     | 78.0 ms: 1.08x slower                                                      |
| json_dumps                 | 5.76 ms                                                     | 6.26 ms: 1.09x slower                                                      |
| sympy_sum                  | 86.4 ms                                                     | 94.0 ms: 1.09x slower                                                      |
| regex_dna                  | 114 ms                                                      | 125 ms: 1.09x slower                                                       |
| async_tree_io_tg           | 512 ms                                                      | 561 ms: 1.09x slower                                                       |
| sympy_expand               | 285 ms                                                      | 312 ms: 1.09x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 42.3 ms: 1.10x slower                                                      |
| dulwich_log                | 40.4 ms                                                     | 44.4 ms: 1.10x slower                                                      |
| create_gc_cycles           | 829 us                                                      | 913 us: 1.10x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.11x slower                                                      |
| sympy_str                  | 166 ms                                                      | 184 ms: 1.11x slower                                                       |
| pylint                     | 211 ms                                                      | 234 ms: 1.11x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 59.1 ms: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| genshi_xml                 | 32.8 ms                                                     | 36.9 ms: 1.13x slower                                                      |
| logging_format             | 6.15 us                                                     | 6.94 us: 1.13x slower                                                      |
| logging_simple             | 5.72 us                                                     | 6.48 us: 1.13x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.79 sec: 1.13x slower                                                     |
| sqlglot_optimize           | 33.1 ms                                                     | 37.6 ms: 1.14x slower                                                      |
| mdp                        | 1.38 sec                                                    | 1.58 sec: 1.14x slower                                                     |
| regex_v8                   | 14.7 ms                                                     | 16.7 ms: 1.14x slower                                                      |
| mako                       | 6.24 ms                                                     | 7.13 ms: 1.14x slower                                                      |
| async_tree_io              | 521 ms                                                      | 599 ms: 1.15x slower                                                       |
| float                      | 48.1 ms                                                     | 55.3 ms: 1.15x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 42.5 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 493 ms                                                      | 573 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 100 us                                                      | 117 us: 1.17x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 94.2 ms: 1.18x slower                                                      |
| scimark_fft                | 174 ms                                                      | 205 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 202 ms: 1.18x slower                                                       |
| pprint_pformat             | 991 ms                                                      | 1.18 sec: 1.19x slower                                                     |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.78 ms: 1.19x slower                                                      |
| go                         | 84.6 ms                                                     | 101 ms: 1.19x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.14 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 127 us                                                      | 152 us: 1.20x slower                                                       |
| sqlglot_parse              | 761 us                                                      | 915 us: 1.20x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 66.8 ms: 1.20x slower                                                      |
| django_template            | 21.8 ms                                                     | 26.2 ms: 1.21x slower                                                      |
| scimark_lu                 | 54.0 ms                                                     | 65.1 ms: 1.21x slower                                                      |
| pyflate                    | 275 ms                                                      | 333 ms: 1.21x slower                                                       |
| chaos                      | 37.9 ms                                                     | 45.8 ms: 1.21x slower                                                      |
| genshi_text                | 14.9 ms                                                     | 18.0 ms: 1.21x slower                                                      |
| crypto_pyaes               | 42.8 ms                                                     | 51.9 ms: 1.21x slower                                                      |
| tomli_loads                | 1.36 sec                                                    | 1.66 sec: 1.22x slower                                                     |
| fannkuch                   | 245 ms                                                      | 298 ms: 1.22x slower                                                       |
| comprehensions             | 10.2 us                                                     | 12.5 us: 1.22x slower                                                      |
| pycparser                  | 758 ms                                                      | 928 ms: 1.22x slower                                                       |
| pickle_pure_python         | 183 us                                                      | 226 us: 1.23x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 2.35 ms: 1.26x slower                                                      |
| hexiom                     | 3.69 ms                                                     | 4.72 ms: 1.28x slower                                                      |
| logging_silent             | 51.0 ns                                                     | 66.1 ns: 1.30x slower                                                      |
| raytrace                   | 156 ms                                                      | 204 ms: 1.30x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 52.5 ms: 1.30x slower                                                      |
| spectral_norm              | 59.2 ms                                                     | 77.3 ms: 1.31x slower                                                      |
| richards_super             | 29.3 ms                                                     | 38.5 ms: 1.31x slower                                                      |
| richards                   | 26.0 ms                                                     | 34.2 ms: 1.32x slower                                                      |
| scimark_sor                | 72.0 ms                                                     | 96.2 ms: 1.34x slower                                                      |
| nbody                      | 64.5 ms                                                     | 91.2 ms: 1.42x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (10): async_tree_none_tg, asyncio_tcp, pathlib, async_tree_memoization, deepcopy_reduce, bench_thread_pool, bench_mp_pool, async_tree_none, python_startup_no_site, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown