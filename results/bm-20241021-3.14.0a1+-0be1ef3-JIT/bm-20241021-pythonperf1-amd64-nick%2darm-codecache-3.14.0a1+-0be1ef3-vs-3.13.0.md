# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: windows-amd64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.01x slower
- HPT reliability: 98.45%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 240 ms: 1.11x slower                                                 |
| docutils       | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                               |
| tornado_http   | 92.8 ms                                                     | 98.0 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                       | 1.08x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                 |
| async_tree_none            | 223 ms                                                      | 218 ms: 1.03x faster                                                 |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.06x slower                                                 |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                 |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.10x slower                                                |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                 |
| async_tree_io_tg           | 512 ms                                                      | 631 ms: 1.23x slower                                                 |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                         |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 53.1 ms: 1.21x faster                                                |
| float          | 48.1 ms                                                     | 47.4 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                |
| regex_v8       | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                |
| regex_dna      | 114 ms                                                      | 122 ms: 1.07x slower                                                 |
| regex_compile  | 80.1 ms                                                     | 86.7 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.24 sec: 1.10x faster                                               |
| xml_etree_generate   | 53.3 ms                                                     | 50.2 ms: 1.06x faster                                                |
| xml_etree_process    | 36.5 ms                                                     | 36.0 ms: 1.01x faster                                                |
| json_loads           | 14.3 us                                                     | 14.5 us: 1.01x slower                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 63.7 ms: 1.02x slower                                                |
| xml_etree_parse      | 93.2 ms                                                     | 95.5 ms: 1.02x slower                                                |
| pickle_pure_python   | 183 us                                                      | 199 us: 1.08x slower                                                 |
| json_dumps           | 5.76 ms                                                     | 6.27 ms: 1.09x slower                                                |
| unpickle_pure_python | 127 us                                                      | 142 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                                |
| python_startup         | 22.2 ms                                                     | 24.2 ms: 1.09x slower                                                |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.08 ms: 1.23x faster                                                |
| genshi_xml      | 32.8 ms                                                     | 38.0 ms: 1.16x slower                                                |
| django_template | 21.8 ms                                                     | 25.3 ms: 1.16x slower                                                |
| genshi_text     | 14.9 ms                                                     | 17.9 ms: 1.20x slower                                                |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 519 us: 16.73x faster                                                |
| deepcopy_memo              | 21.8 us                                                     | 15.8 us: 1.38x faster                                                |
| mako                       | 6.24 ms                                                     | 5.08 ms: 1.23x faster                                                |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                 |
| nbody                      | 64.5 ms                                                     | 53.1 ms: 1.21x faster                                                |
| fannkuch                   | 245 ms                                                      | 212 ms: 1.16x faster                                                 |
| pprint_safe_repr           | 493 ms                                                      | 433 ms: 1.14x faster                                                 |
| scimark_sor                | 72.0 ms                                                     | 63.7 ms: 1.13x faster                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                |
| scimark_monte_carlo        | 40.3 ms                                                     | 36.1 ms: 1.12x faster                                                |
| scimark_fft                | 174 ms                                                      | 157 ms: 1.11x faster                                                 |
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                 |
| tomli_loads                | 1.36 sec                                                    | 1.24 sec: 1.10x faster                                               |
| pprint_pformat             | 991 ms                                                      | 906 ms: 1.09x faster                                                 |
| pycparser                  | 758 ms                                                      | 696 ms: 1.09x faster                                                 |
| crypto_pyaes               | 42.8 ms                                                     | 39.9 ms: 1.07x faster                                                |
| spectral_norm              | 59.2 ms                                                     | 55.7 ms: 1.06x faster                                                |
| xml_etree_generate         | 53.3 ms                                                     | 50.2 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.21 ms: 1.06x faster                                                |
| telco                      | 4.85 ms                                                     | 4.57 ms: 1.06x faster                                                |
| go                         | 84.6 ms                                                     | 82.2 ms: 1.03x faster                                                |
| async_tree_none            | 223 ms                                                      | 218 ms: 1.03x faster                                                 |
| xml_etree_process          | 36.5 ms                                                     | 36.0 ms: 1.01x faster                                                |
| float                      | 48.1 ms                                                     | 47.4 ms: 1.01x faster                                                |
| json                       | 2.98 ms                                                     | 2.94 ms: 1.01x faster                                                |
| dulwich_log                | 40.4 ms                                                     | 39.9 ms: 1.01x faster                                                |
| pathlib                    | 81.2 ms                                                     | 80.3 ms: 1.01x faster                                                |
| pyflate                    | 275 ms                                                      | 274 ms: 1.01x faster                                                 |
| meteor_contest             | 72.3 ms                                                     | 71.9 ms: 1.01x faster                                                |
| json_loads                 | 14.3 us                                                     | 14.5 us: 1.01x slower                                                |
| async_tree_none_tg         | 206 ms                                                      | 209 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 62.3 ms                                                     | 63.7 ms: 1.02x slower                                                |
| coverage                   | 46.7 ms                                                     | 47.8 ms: 1.02x slower                                                |
| xml_etree_parse            | 93.2 ms                                                     | 95.5 ms: 1.02x slower                                                |
| regex_effbot               | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                                |
| python_startup_no_site     | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                                |
| logging_format             | 6.15 us                                                     | 6.44 us: 1.05x slower                                                |
| sympy_expand               | 285 ms                                                      | 300 ms: 1.05x slower                                                 |
| tornado_http               | 92.8 ms                                                     | 98.0 ms: 1.06x slower                                                |
| logging_simple             | 5.72 us                                                     | 6.05 us: 1.06x slower                                                |
| regex_v8                   | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                                |
| comprehensions             | 10.2 us                                                     | 10.9 us: 1.06x slower                                                |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 399 ms: 1.06x slower                                                 |
| regex_dna                  | 114 ms                                                      | 122 ms: 1.07x slower                                                 |
| logging_silent             | 51.0 ns                                                     | 54.6 ns: 1.07x slower                                                |
| sympy_str                  | 166 ms                                                      | 179 ms: 1.08x slower                                                 |
| regex_compile              | 80.1 ms                                                     | 86.7 ms: 1.08x slower                                                |
| pickle_pure_python         | 183 us                                                      | 199 us: 1.08x slower                                                 |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                 |
| json_dumps                 | 5.76 ms                                                     | 6.27 ms: 1.09x slower                                                |
| python_startup             | 22.2 ms                                                     | 24.2 ms: 1.09x slower                                                |
| mdp                        | 1.38 sec                                                    | 1.53 sec: 1.10x slower                                               |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.10x slower                                                |
| 2to3                       | 217 ms                                                      | 240 ms: 1.11x slower                                                 |
| generators                 | 19.5 ms                                                     | 21.6 ms: 1.11x slower                                                |
| sqlglot_parse              | 761 us                                                      | 850 us: 1.12x slower                                                 |
| unpickle_pure_python       | 127 us                                                      | 142 us: 1.12x slower                                                 |
| nqueens                    | 55.5 ms                                                     | 62.7 ms: 1.13x slower                                                |
| sqlglot_normalize          | 171 ms                                                      | 194 ms: 1.13x slower                                                 |
| sympy_sum                  | 86.4 ms                                                     | 98.0 ms: 1.13x slower                                                |
| typing_runtime_protocols   | 100 us                                                      | 114 us: 1.14x slower                                                 |
| genshi_xml                 | 32.8 ms                                                     | 38.0 ms: 1.16x slower                                                |
| hexiom                     | 3.69 ms                                                     | 4.28 ms: 1.16x slower                                                |
| django_template            | 21.8 ms                                                     | 25.3 ms: 1.16x slower                                                |
| sqlglot_transpile          | 952 us                                                      | 1.11 ms: 1.17x slower                                                |
| docutils                   | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                               |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                 |
| richards                   | 26.0 ms                                                     | 30.8 ms: 1.18x slower                                                |
| sqlglot_optimize           | 33.1 ms                                                     | 39.4 ms: 1.19x slower                                                |
| deltablue                  | 1.86 ms                                                     | 2.23 ms: 1.19x slower                                                |
| richards_super             | 29.3 ms                                                     | 35.0 ms: 1.19x slower                                                |
| genshi_text                | 14.9 ms                                                     | 17.9 ms: 1.20x slower                                                |
| sympy_integrate            | 12.3 ms                                                     | 15.0 ms: 1.22x slower                                                |
| async_tree_io_tg           | 512 ms                                                      | 631 ms: 1.23x slower                                                 |
| gc_traversal               | 1.55 ms                                                     | 1.94 ms: 1.25x slower                                                |
| pylint                     | 211 ms                                                      | 268 ms: 1.27x slower                                                 |
| bench_mp_pool              | 69.6 ms                                                     | 89.1 ms: 1.28x slower                                                |
| raytrace                   | 156 ms                                                      | 200 ms: 1.28x slower                                                 |
| create_gc_cycles           | 829 us                                                      | 1.39 ms: 1.68x slower                                                |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (6): pidigits, html5lib, scimark_lu, async_tree_cpu_io_mixed, async_tree_memoization, bench_thread_pool
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: sphinx

# HPT report

- Reliability score: 98.45% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown