# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 7e6deef
- commit date: 2024-10-29
- overall geometric mean: 1.311x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 530 ms: 1.52x slower                                                      |
| docutils       | 3.30 sec                                               | 5.45 sec: 1.65x slower                                                    |
| html5lib       | 88.9 ms                                                | 130 ms: 1.46x slower                                                      |
| tornado_http   | 136 ms                                                 | 187 ms: 1.37x slower                                                      |
| Geometric mean | (ref)                                                  | 1.50x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 687 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 1.17 sec: 1.15x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (2): async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 195 ms: 1.27x slower                                                      |
| float          | 117 ms                                                 | 161 ms: 1.38x slower                                                      |
| pidigits       | 191 ms                                                 | 378 ms: 1.98x slower                                                      |
| Geometric mean | (ref)                                                  | 1.51x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 264 ms: 1.40x slower                                                      |
| regex_v8       | 27.8 ms                                                | 49.1 ms: 1.77x slower                                                     |
| regex_dna      | 227 ms                                                 | 439 ms: 1.94x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 7.47 ms: 2.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.77x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 635 us: 1.31x slower                                                      |
| unpickle_pure_python | 331 us                                                 | 445 us: 1.35x slower                                                      |
| tomli_loads          | 3.14 sec                                               | 4.25 sec: 1.35x slower                                                    |
| xml_etree_process    | 79.1 ms                                                | 123 ms: 1.55x slower                                                      |
| json_dumps           | 14.2 ms                                                | 23.2 ms: 1.64x slower                                                     |
| json_loads           | 31.2 us                                                | 53.4 us: 1.71x slower                                                     |
| xml_etree_generate   | 99.4 ms                                                | 177 ms: 1.78x slower                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 206 ms: 1.78x slower                                                      |
| xml_etree_parse      | 168 ms                                                 | 314 ms: 1.87x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.58x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 31.0 ms: 2.13x slower                                                     |
| python_startup_no_site | 5.93 ms                                                | 15.7 ms: 2.65x slower                                                     |
| Geometric mean         | (ref)                                                  | 2.37x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 45.3 ms: 1.42x slower                                                     |
| mako            | 16.3 ms                                                | 23.3 ms: 1.43x slower                                                     |
| django_template | 48.2 ms                                                | 72.1 ms: 1.50x slower                                                     |
| genshi_xml      | 66.0 ms                                                | 104 ms: 1.58x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.48x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 331 us: 1.65x faster                                                      |
| generators               | 80.1 ms                                                | 58.8 ms: 1.36x faster                                                     |
| deltablue                | 7.91 ms                                                | 6.46 ms: 1.23x faster                                                     |
| async_tree_none          | 728 ms                                                 | 687 ms: 1.06x faster                                                      |
| logging_silent           | 190 ns                                                 | 193 ns: 1.02x slower                                                      |
| raytrace                 | 507 ms                                                 | 542 ms: 1.07x slower                                                      |
| chaos                    | 115 ms                                                 | 126 ms: 1.09x slower                                                      |
| deepcopy                 | 479 us                                                 | 533 us: 1.11x slower                                                      |
| richards_super           | 94.7 ms                                                | 105 ms: 1.11x slower                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 1.17 sec: 1.15x slower                                                    |
| richards                 | 79.3 ms                                                | 92.4 ms: 1.17x slower                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 138 ms: 1.17x slower                                                      |
| crypto_pyaes             | 128 ms                                                 | 150 ms: 1.17x slower                                                      |
| pylint                   | 551 ms                                                 | 653 ms: 1.18x slower                                                      |
| sqlglot_parse            | 2.17 ms                                                | 2.62 ms: 1.21x slower                                                     |
| comprehensions           | 28.8 us                                                | 34.9 us: 1.21x slower                                                     |
| scimark_sor              | 220 ms                                                 | 270 ms: 1.23x slower                                                      |
| hexiom                   | 10.4 ms                                                | 12.9 ms: 1.24x slower                                                     |
| nbody                    | 154 ms                                                 | 195 ms: 1.27x slower                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 3.28 ms: 1.28x slower                                                     |
| pickle_pure_python       | 484 us                                                 | 635 us: 1.31x slower                                                      |
| scimark_lu               | 176 ms                                                 | 232 ms: 1.32x slower                                                      |
| unpickle_pure_python     | 331 us                                                 | 445 us: 1.35x slower                                                      |
| deepcopy_reduce          | 4.17 us                                                | 5.62 us: 1.35x slower                                                     |
| spectral_norm            | 170 ms                                                 | 230 ms: 1.35x slower                                                      |
| tomli_loads              | 3.14 sec                                               | 4.25 sec: 1.35x slower                                                    |
| tornado_http             | 136 ms                                                 | 187 ms: 1.37x slower                                                      |
| float                    | 117 ms                                                 | 161 ms: 1.38x slower                                                      |
| pyflate                  | 716 ms                                                 | 987 ms: 1.38x slower                                                      |
| regex_compile            | 188 ms                                                 | 264 ms: 1.40x slower                                                      |
| genshi_text              | 31.8 ms                                                | 45.3 ms: 1.42x slower                                                     |
| mako                     | 16.3 ms                                                | 23.3 ms: 1.43x slower                                                     |
| coroutines               | 35.1 ms                                                | 50.5 ms: 1.44x slower                                                     |
| logging_simple           | 8.30 us                                                | 11.9 us: 1.44x slower                                                     |
| logging_format           | 9.09 us                                                | 13.2 us: 1.45x slower                                                     |
| html5lib                 | 88.9 ms                                                | 130 ms: 1.46x slower                                                      |
| pprint_pformat           | 2.10 sec                                               | 3.07 sec: 1.46x slower                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 1.50 sec: 1.47x slower                                                    |
| thrift                   | 1.07 ms                                                | 1.59 ms: 1.49x slower                                                     |
| django_template          | 48.2 ms                                                | 72.1 ms: 1.50x slower                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 35.3 ms: 1.51x slower                                                     |
| 2to3                     | 348 ms                                                 | 530 ms: 1.52x slower                                                      |
| pycparser                | 1.58 sec                                               | 2.41 sec: 1.53x slower                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 264 ms: 1.53x slower                                                      |
| sqlglot_normalize        | 143 ms                                                 | 219 ms: 1.54x slower                                                      |
| dulwich_log              | 84.3 ms                                                | 130 ms: 1.54x slower                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 9.96 ms: 1.54x slower                                                     |
| sympy_sum                | 196 ms                                                 | 303 ms: 1.54x slower                                                      |
| xml_etree_process        | 79.1 ms                                                | 123 ms: 1.55x slower                                                      |
| sympy_integrate          | 25.8 ms                                                | 40.5 ms: 1.57x slower                                                     |
| genshi_xml               | 66.0 ms                                                | 104 ms: 1.58x slower                                                      |
| pathlib                  | 20.5 ms                                                | 32.6 ms: 1.59x slower                                                     |
| sympy_str                | 346 ms                                                 | 553 ms: 1.60x slower                                                      |
| scimark_fft              | 466 ms                                                 | 746 ms: 1.60x slower                                                      |
| fannkuch                 | 532 ms                                                 | 859 ms: 1.62x slower                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 112 ms: 1.62x slower                                                      |
| json_dumps               | 14.2 ms                                                | 23.2 ms: 1.64x slower                                                     |
| nqueens                  | 106 ms                                                 | 173 ms: 1.64x slower                                                      |
| docutils                 | 3.30 sec                                               | 5.45 sec: 1.65x slower                                                    |
| sympy_expand             | 566 ms                                                 | 943 ms: 1.67x slower                                                      |
| json_loads               | 31.2 us                                                | 53.4 us: 1.71x slower                                                     |
| json                     | 5.69 ms                                                | 9.80 ms: 1.72x slower                                                     |
| mdp                      | 2.85 sec                                               | 5.02 sec: 1.76x slower                                                    |
| regex_v8                 | 27.8 ms                                                | 49.1 ms: 1.77x slower                                                     |
| xml_etree_generate       | 99.4 ms                                                | 177 ms: 1.78x slower                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 206 ms: 1.78x slower                                                      |
| meteor_contest           | 120 ms                                                 | 216 ms: 1.80x slower                                                      |
| xml_etree_parse          | 168 ms                                                 | 314 ms: 1.87x slower                                                      |
| regex_dna                | 227 ms                                                 | 439 ms: 1.94x slower                                                      |
| asyncio_websockets       | 559 ms                                                 | 1.11 sec: 1.98x slower                                                    |
| pidigits                 | 191 ms                                                 | 378 ms: 1.98x slower                                                      |
| async_generators         | 444 ms                                                 | 882 ms: 1.99x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 7.47 ms: 2.06x slower                                                     |
| coverage                 | 79.4 ms                                                | 167 ms: 2.11x slower                                                      |
| python_startup           | 14.6 ms                                                | 31.0 ms: 2.13x slower                                                     |
| telco                    | 7.27 ms                                                | 16.2 ms: 2.23x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 8.77 ms: 2.42x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 15.7 ms: 2.65x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 5.24 ms: 3.23x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 128 ms: 5.32x slower                                                      |
| bench_thread_pool        | 986 us                                                 | 30.3 ms: 30.70x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.52x slower                                                              |

Benchmark hidden because not significant (4): async_tree_io, deepcopy_memo, go, async_tree_memoization
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241029-3.14.0a1+-7e6deef/bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.311x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.43x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.37x

# Memory
- memory change: 1.24x