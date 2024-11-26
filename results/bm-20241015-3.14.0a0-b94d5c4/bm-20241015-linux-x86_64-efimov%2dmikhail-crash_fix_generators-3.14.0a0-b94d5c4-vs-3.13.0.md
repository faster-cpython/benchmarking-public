# Results vs. 3.13.0

- fork: efimov-mikhail
- ref: crash_fix_generators
- machine: linux-x86_64
- commit hash: b94d5c4
- commit date: 2024-10-15
- overall geometric mean: 1.030x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 253 ms: 1.05x faster                                                            |
| docutils       | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                          |
| html5lib       | 64.2 ms                                                | 61.1 ms: 1.05x faster                                                           |
| tornado_http   | 92.4 ms                                                | 90.6 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators | 436 ms                                                 | 440 ms: 1.01x slower                                                            |
| coroutines       | 22.7 ms                                                | 24.0 ms: 1.06x slower                                                           |
| Geometric mean   | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.0 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| nbody          | 87.0 ms                                                | 89.4 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.08x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.49 ms: 1.07x faster                                                           |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                                            |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                           |
| tomli_loads          | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                                           |
| xml_etree_generate   | 86.7 ms                                                | 85.5 ms: 1.01x faster                                                           |
| pickle_pure_python   | 310 us                                                 | 308 us: 1.01x faster                                                            |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.02x slower                                                            |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                           |
| genshi_text     | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 50.0 ms: 1.02x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                 | 358 us                                                 | 264 us: 1.36x faster                                                            |
| create_gc_cycles         | 2.41 ms                                                | 1.79 ms: 1.35x faster                                                           |
| deepcopy_memo            | 39.1 us                                                | 31.2 us: 1.25x faster                                                           |
| go                       | 144 ms                                                 | 120 ms: 1.20x faster                                                            |
| deepcopy_reduce          | 3.20 us                                                | 2.70 us: 1.19x faster                                                           |
| python_startup           | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                           |
| pathlib                  | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                           |
| mdp                      | 2.72 sec                                               | 2.49 sec: 1.09x faster                                                          |
| gc_traversal             | 4.37 ms                                                | 4.02 ms: 1.09x faster                                                           |
| regex_v8                 | 26.2 ms                                                | 24.4 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult  | 5.04 ms                                                | 4.70 ms: 1.07x faster                                                           |
| telco                    | 8.54 ms                                                | 7.98 ms: 1.07x faster                                                           |
| regex_effbot             | 3.73 ms                                                | 3.49 ms: 1.07x faster                                                           |
| richards                 | 48.7 ms                                                | 45.9 ms: 1.06x faster                                                           |
| 2to3                     | 267 ms                                                 | 253 ms: 1.05x faster                                                            |
| richards_super           | 54.9 ms                                                | 52.1 ms: 1.05x faster                                                           |
| thrift                   | 809 us                                                 | 770 us: 1.05x faster                                                            |
| html5lib                 | 64.2 ms                                                | 61.1 ms: 1.05x faster                                                           |
| json                     | 5.36 ms                                                | 5.12 ms: 1.05x faster                                                           |
| generators               | 29.0 ms                                                | 27.8 ms: 1.04x faster                                                           |
| django_template          | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                           |
| meteor_contest           | 109 ms                                                 | 105 ms: 1.03x faster                                                            |
| genshi_text              | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                           |
| logging_simple           | 5.72 us                                                | 5.55 us: 1.03x faster                                                           |
| pyflate                  | 471 ms                                                 | 457 ms: 1.03x faster                                                            |
| regex_dna                | 218 ms                                                 | 212 ms: 1.03x faster                                                            |
| pycparser                | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                          |
| crypto_pyaes             | 75.3 ms                                                | 73.2 ms: 1.03x faster                                                           |
| regex_compile            | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| sympy_str                | 275 ms                                                 | 268 ms: 1.03x faster                                                            |
| logging_format           | 6.40 us                                                | 6.25 us: 1.02x faster                                                           |
| typing_runtime_protocols | 165 us                                                 | 161 us: 1.02x faster                                                            |
| xml_etree_process        | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                           |
| tornado_http             | 92.4 ms                                                | 90.6 ms: 1.02x faster                                                           |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.02x faster                                                            |
| sympy_sum                | 150 ms                                                 | 148 ms: 1.02x faster                                                            |
| tomli_loads              | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| genshi_xml               | 50.9 ms                                                | 50.0 ms: 1.02x faster                                                           |
| json_loads               | 27.2 us                                                | 26.8 us: 1.02x faster                                                           |
| float                    | 79.2 ms                                                | 78.0 ms: 1.02x faster                                                           |
| xml_etree_generate       | 86.7 ms                                                | 85.5 ms: 1.01x faster                                                           |
| scimark_fft              | 364 ms                                                 | 360 ms: 1.01x faster                                                            |
| sqlglot_optimize         | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                           |
| sympy_expand             | 463 ms                                                 | 458 ms: 1.01x faster                                                            |
| pprint_safe_repr         | 728 ms                                                 | 720 ms: 1.01x faster                                                            |
| pprint_pformat           | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                          |
| pickle_pure_python       | 310 us                                                 | 308 us: 1.01x faster                                                            |
| bpe_tokeniser            | 4.75 sec                                               | 4.71 sec: 1.01x faster                                                          |
| sympy_integrate          | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                           |
| scimark_monte_carlo      | 67.4 ms                                                | 67.8 ms: 1.00x slower                                                           |
| unpickle_pure_python     | 216 us                                                 | 217 us: 1.01x slower                                                            |
| pidigits                 | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| dulwich_log              | 64.3 ms                                                | 64.7 ms: 1.01x slower                                                           |
| docutils                 | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                          |
| async_generators         | 436 ms                                                 | 440 ms: 1.01x slower                                                            |
| python_startup_no_site   | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                           |
| sqlglot_transpile        | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                           |
| deltablue                | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                           |
| comprehensions           | 16.5 us                                                | 16.7 us: 1.02x slower                                                           |
| mako                     | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| spectral_norm            | 115 ms                                                 | 117 ms: 1.02x slower                                                            |
| scimark_lu               | 113 ms                                                 | 115 ms: 1.02x slower                                                            |
| bench_thread_pool        | 822 us                                                 | 837 us: 1.02x slower                                                            |
| sqlglot_parse            | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                           |
| logging_silent           | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| xml_etree_iterparse      | 101 ms                                                 | 104 ms: 1.02x slower                                                            |
| hexiom                   | 6.16 ms                                                | 6.31 ms: 1.02x slower                                                           |
| nqueens                  | 78.4 ms                                                | 80.5 ms: 1.03x slower                                                           |
| scimark_sor              | 124 ms                                                 | 127 ms: 1.03x slower                                                            |
| nbody                    | 87.0 ms                                                | 89.4 ms: 1.03x slower                                                           |
| chaos                    | 58.1 ms                                                | 60.9 ms: 1.05x slower                                                           |
| coroutines               | 22.7 ms                                                | 24.0 ms: 1.06x slower                                                           |
| json_dumps               | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.0 ms: 2.33x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (6): fannkuch, xml_etree_parse, coverage, asyncio_websockets, raytrace, pylint
Ignored benchmarks (17) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a0-b94d5c4/bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x