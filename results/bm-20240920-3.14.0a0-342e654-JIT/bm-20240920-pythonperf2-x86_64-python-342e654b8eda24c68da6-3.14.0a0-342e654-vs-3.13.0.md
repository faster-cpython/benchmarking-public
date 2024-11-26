# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.027x faster
- HPT reliability: 95.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 310 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.3 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                       | 121 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 801 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 801 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 81.1 ms: 1.14x faster                                                       |
| float          | 81.6 ms                                                      | 73.7 ms: 1.11x faster                                                       |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                       |
| regex_dna      | 238 ms                                                       | 235 ms: 1.01x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                                       |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.12 sec: 1.15x faster                                                      |
| xml_etree_process    | 60.7 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 78.7 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 98.3 ms: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 213 us: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| pickle_pure_python   | 322 us                                                       | 328 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.10 ms: 1.13x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 28.3 ms: 1.04x slower                                                       |
| genshi_xml      | 58.0 ms                                                      | 62.3 ms: 1.07x slower                                                       |
| django_template | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 26.9 us: 1.45x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 1.91 ms: 1.39x faster                                                       |
| deepcopy                   | 388 us                                                       | 289 us: 1.34x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.88 us: 1.21x faster                                                       |
| scimark_sor                | 125 ms                                                       | 104 ms: 1.20x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 82.3 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| richards                   | 52.5 ms                                                      | 44.9 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.12 sec: 1.15x faster                                                      |
| richards_super             | 60.2 ms                                                      | 52.9 ms: 1.14x faster                                                       |
| nbody                      | 92.1 ms                                                      | 81.1 ms: 1.14x faster                                                       |
| mako                       | 10.3 ms                                                      | 9.10 ms: 1.13x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| float                      | 81.6 ms                                                      | 73.7 ms: 1.11x faster                                                       |
| go                         | 167 ms                                                       | 151 ms: 1.11x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.05 ms: 1.09x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 78.7 ms: 1.08x faster                                                       |
| json                       | 5.62 ms                                                      | 5.20 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.78 sec: 1.07x faster                                                      |
| fannkuch                   | 384 ms                                                       | 361 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.96 ms: 1.06x faster                                                       |
| deltablue                  | 3.38 ms                                                      | 3.19 ms: 1.06x faster                                                       |
| pyflate                    | 493 ms                                                       | 465 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 789 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| scimark_fft                | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                      |
| coverage                   | 84.5 ms                                                      | 81.1 ms: 1.04x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 70.6 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 801 ms: 1.04x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 70.3 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 801 ms: 1.03x faster                                                        |
| thrift                     | 918 us                                                       | 896 us: 1.02x faster                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.40 ms: 1.02x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 98.3 ms: 1.02x faster                                                       |
| regex_dna                  | 238 ms                                                       | 235 ms: 1.01x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 216 us                                                       | 213 us: 1.01x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 96.5 ms: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                       |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                                       |
| tornado_http               | 119 ms                                                       | 121 ms: 1.02x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 328 us: 1.02x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 179 us: 1.02x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.59 sec: 1.02x slower                                                      |
| logging_format             | 6.95 us                                                      | 7.13 us: 1.03x slower                                                       |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                        |
| sympy_expand               | 506 ms                                                       | 524 ms: 1.04x slower                                                        |
| sympy_str                  | 297 ms                                                       | 309 ms: 1.04x slower                                                        |
| genshi_text                | 27.2 ms                                                      | 28.3 ms: 1.04x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.54 us: 1.04x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 102 ns: 1.04x slower                                                        |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.1 us: 1.05x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 97.2 ms: 1.05x slower                                                       |
| 2to3                       | 293 ms                                                       | 310 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.2 ms: 1.06x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 5.17 ms: 1.07x slower                                                       |
| genshi_xml                 | 58.0 ms                                                      | 62.3 ms: 1.07x slower                                                       |
| hexiom                     | 6.47 ms                                                      | 6.95 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 129 ms: 1.08x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.48 ms: 1.09x slower                                                       |
| generators                 | 33.9 ms                                                      | 36.9 ms: 1.09x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 168 ms: 1.09x slower                                                        |
| chaos                      | 60.6 ms                                                      | 66.6 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| django_template            | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 65.6 ms: 1.12x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 26.3 ms: 1.12x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| raytrace                   | 267 ms                                                       | 316 ms: 1.18x slower                                                        |
| pylint                     | 345 ms                                                       | 409 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (5): asyncio_websockets, xml_etree_parse, pycparser, json_loads, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 95.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x