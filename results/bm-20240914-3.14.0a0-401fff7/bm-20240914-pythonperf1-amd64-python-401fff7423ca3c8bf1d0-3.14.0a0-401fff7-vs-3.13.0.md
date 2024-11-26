# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 225 ms: 1.02x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.6 ms: 1.04x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 83.5 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| async_tree_none            | 226 ms                                                      | 211 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 263 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 203 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 393 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 565 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 55.9 ms: 1.12x slower                                                      |
| nbody          | 68.4 ms                                                     | 83.3 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                      |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 92.3 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 6.23 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.2 ms: 1.06x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 59.0 ms: 1.09x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 41.5 ms: 1.12x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 216 us: 1.14x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.63 sec: 1.17x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.0 ms: 1.15x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 36.8 ms: 1.04x slower                                                      |
| mako            | 6.35 ms                                                     | 6.82 ms: 1.07x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| django_template | 22.4 ms                                                     | 26.0 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 513 us: 17.15x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 874 us: 1.44x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 66.2 ms: 1.31x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.52 ms: 1.29x faster                                                      |
| deepcopy                   | 226 us                                                      | 188 us: 1.20x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.0 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| tornado_http               | 93.0 ms                                                     | 83.5 ms: 1.11x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 21.0 us: 1.11x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 74.6 ms: 1.08x faster                                                      |
| json                       | 3.19 ms                                                     | 2.98 ms: 1.07x faster                                                      |
| async_tree_none            | 226 ms                                                      | 211 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.93 us: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 263 ms: 1.05x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 813 us: 1.04x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 203 ms: 1.03x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                                      |
| go                         | 87.0 ms                                                     | 87.8 ms: 1.01x slower                                                      |
| 2to3                       | 221 ms                                                      | 225 ms: 1.02x slower                                                       |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 89.7 ms: 1.03x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 42.3 ms: 1.04x slower                                                      |
| genshi_xml                 | 35.5 ms                                                     | 36.8 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 393 ms: 1.04x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.6 ms: 1.04x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.01 ms: 1.05x slower                                                      |
| coverage                   | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.23 ms: 1.05x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 47.9 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.2 ms: 1.06x slower                                                      |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                       |
| sympy_expand               | 291 ms                                                      | 308 ms: 1.06x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.31 us: 1.06x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 78.0 ms: 1.06x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.82 ms: 1.07x slower                                                      |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.07x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| async_tree_io_tg           | 518 ms                                                      | 565 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 115 us: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 59.0 ms: 1.09x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.90 us: 1.10x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.53 sec: 1.10x slower                                                     |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.5 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 551 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 195 ms: 1.12x slower                                                       |
| float                      | 49.9 ms                                                     | 55.9 ms: 1.12x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 41.5 ms: 1.12x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.79 ms: 1.13x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.13 sec: 1.14x slower                                                     |
| nqueens                    | 56.7 ms                                                     | 64.5 ms: 1.14x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 216 us: 1.14x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.0 ms: 1.14x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 92.3 ms: 1.15x slower                                                      |
| pyflate                    | 283 ms                                                      | 326 ms: 1.15x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.0 ms: 1.16x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.63 sec: 1.17x slower                                                     |
| spectral_norm              | 62.8 ms                                                     | 73.6 ms: 1.17x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 905 us: 1.17x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.57 ms: 1.18x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.13 ms: 1.18x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 64.8 ns: 1.19x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.4 ms: 1.19x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 62.9 ms: 1.19x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.7 ms: 1.19x slower                                                      |
| comprehensions             | 10.3 us                                                     | 12.2 us: 1.19x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.29 ms: 1.19x slower                                                      |
| fannkuch                   | 253 ms                                                      | 302 ms: 1.19x slower                                                       |
| scimark_fft                | 172 ms                                                      | 206 ms: 1.20x slower                                                       |
| pycparser                  | 683 ms                                                      | 826 ms: 1.21x slower                                                       |
| nbody                      | 68.4 ms                                                     | 83.3 ms: 1.22x slower                                                      |
| raytrace                   | 160 ms                                                      | 195 ms: 1.22x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 50.2 ms: 1.23x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 93.9 ms: 1.23x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, async_tree_cpu_io_mixed, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown