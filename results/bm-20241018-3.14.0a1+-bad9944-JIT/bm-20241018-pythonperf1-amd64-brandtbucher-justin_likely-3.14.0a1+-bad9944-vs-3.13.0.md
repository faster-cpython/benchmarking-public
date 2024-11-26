# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: windows-amd64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.015x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 250 ms: 1.13x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                     |
| sphinx         | 633 ms                                                      | 767 ms: 1.21x slower                                                       |
| tornado_http   | 93.0 ms                                                     | 99.5 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                       |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                       |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 632 ms: 1.22x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 55.0 ms: 1.24x faster                                                      |
| float          | 49.9 ms                                                     | 46.5 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                                      |
| regex_compile  | 80.5 ms                                                     | 92.9 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                                     |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 51.5 ms: 1.05x faster                                                      |
| xml_etree_process    | 37.0 ms                                                     | 36.5 ms: 1.01x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.16 ms: 1.04x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 198 us: 1.05x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 143 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.4 ms: 1.04x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 18.7 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.13 ms: 1.24x faster                                                      |
| django_template | 22.4 ms                                                     | 27.7 ms: 1.24x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 19.4 ms: 1.24x slower                                                      |
| genshi_xml      | 35.5 ms                                                     | 46.0 ms: 1.30x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 527 us: 16.68x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 16.8 us: 1.39x faster                                                      |
| nbody                      | 68.4 ms                                                     | 55.0 ms: 1.24x faster                                                      |
| mako                       | 6.35 ms                                                     | 5.13 ms: 1.24x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 65.1 ms: 1.17x faster                                                      |
| deepcopy                   | 226 us                                                      | 194 us: 1.17x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 53.9 ms: 1.17x faster                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 40.8 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.23 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 37.1 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.88 us: 1.09x faster                                                      |
| scimark_fft                | 172 ms                                                      | 157 ms: 1.09x faster                                                       |
| json                       | 3.19 ms                                                     | 2.95 ms: 1.08x faster                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                                     |
| float                      | 49.9 ms                                                     | 46.5 ms: 1.07x faster                                                      |
| fannkuch                   | 253 ms                                                      | 240 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| telco                      | 4.79 ms                                                     | 4.56 ms: 1.05x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 51.5 ms: 1.05x faster                                                      |
| python_startup             | 25.4 ms                                                     | 24.4 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 494 ms                                                      | 480 ms: 1.03x faster                                                       |
| pprint_pformat             | 999 ms                                                      | 972 ms: 1.03x faster                                                       |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 36.5 ms: 1.01x faster                                                      |
| dulwich_log                | 40.8 ms                                                     | 41.2 ms: 1.01x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 95.9 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 56.1 ns: 1.03x slower                                                      |
| python_startup_no_site     | 18.1 ms                                                     | 18.7 ms: 1.03x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 76.0 ms: 1.03x slower                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 89.7 ms: 1.04x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.16 ms: 1.04x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 55.2 ms: 1.04x slower                                                      |
| pyflate                    | 283 ms                                                      | 296 ms: 1.05x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 198 us: 1.05x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.25 us: 1.05x slower                                                      |
| go                         | 87.0 ms                                                     | 92.0 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                       |
| async_tree_io              | 521 ms                                                      | 554 ms: 1.06x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.67 us: 1.07x slower                                                      |
| tornado_http               | 93.0 ms                                                     | 99.5 ms: 1.07x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 143 us: 1.07x slower                                                       |
| coverage                   | 45.6 ms                                                     | 49.2 ms: 1.08x slower                                                      |
| pycparser                  | 683 ms                                                      | 740 ms: 1.08x slower                                                       |
| chaos                      | 38.5 ms                                                     | 42.2 ms: 1.10x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.53 sec: 1.10x slower                                                     |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 118 us: 1.12x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.41 ms: 1.12x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 63.7 ms: 1.12x slower                                                      |
| 2to3                       | 221 ms                                                      | 250 ms: 1.13x slower                                                       |
| sympy_expand               | 291 ms                                                      | 332 ms: 1.14x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 92.9 ms: 1.15x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                      |
| sympy_str                  | 169 ms                                                      | 195 ms: 1.16x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 908 us: 1.18x slower                                                       |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 104 ms: 1.20x slower                                                       |
| sphinx                     | 633 ms                                                      | 767 ms: 1.21x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 212 ms: 1.21x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 632 ms: 1.22x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.35 ms: 1.23x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                                     |
| generators                 | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                      |
| django_template            | 22.4 ms                                                     | 27.7 ms: 1.24x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 19.4 ms: 1.24x slower                                                      |
| richards_super             | 30.9 ms                                                     | 38.6 ms: 1.25x slower                                                      |
| richards                   | 27.3 ms                                                     | 34.3 ms: 1.25x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.21 ms: 1.27x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 15.9 ms: 1.27x slower                                                      |
| genshi_xml                 | 35.5 ms                                                     | 46.0 ms: 1.30x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 43.4 ms: 1.32x slower                                                      |
| raytrace                   | 160 ms                                                      | 213 ms: 1.33x slower                                                       |
| pylint                     | 211 ms                                                      | 282 ms: 1.34x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 5.25 ms: 1.35x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (8): gc_traversal, bench_thread_pool, html5lib, pathlib, pidigits, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.015x slower
# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown