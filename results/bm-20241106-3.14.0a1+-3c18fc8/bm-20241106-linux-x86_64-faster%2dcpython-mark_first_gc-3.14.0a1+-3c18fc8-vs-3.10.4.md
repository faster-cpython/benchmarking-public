# Results vs. 3.10.4

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 3c18fc8
- commit date: 2024-11-06
- overall geometric mean: 1.446x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                      |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.25x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                                      |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.80x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 334 ms: 2.60x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 95.3 ms: 1.61x faster                                                     |
| float          | 117 ms                                                 | 78.4 ms: 1.49x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                     |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                     |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.3 ms: 1.18x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 6.78 ms: 1.14x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                     |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                      |
| generators               | 80.1 ms                                                | 26.7 ms: 3.00x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                                      |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.80x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 334 ms: 2.60x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                                     |
| pylint                   | 551 ms                                                 | 262 ms: 2.11x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                      |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                      |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 31.3 us: 1.87x faster                                                     |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                      |
| richards_super           | 94.7 ms                                                | 52.3 ms: 1.81x faster                                                     |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                      |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 73.4 ms: 1.74x faster                                                     |
| richards                 | 79.3 ms                                                | 45.5 ms: 1.74x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                     |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.28 ms: 1.65x faster                                                     |
| nbody                    | 154 ms                                                 | 95.3 ms: 1.61x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 2.32 ms: 1.56x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.54x faster                                                     |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                     |
| float                    | 117 ms                                                 | 78.4 ms: 1.49x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                      |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                    |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                                      |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                      |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.42x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                    |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                     |
| thrift                   | 1.07 ms                                                | 768 us: 1.40x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                     |
| html5lib                 | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                     |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                     |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                                     |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                     |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.19 ms: 1.25x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.25x faster                                                    |
| scimark_fft              | 466 ms                                                 | 375 ms: 1.24x faster                                                      |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                      |
| json                     | 5.69 ms                                                | 4.76 ms: 1.20x faster                                                     |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.3 ms: 1.18x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 841 us: 1.17x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                                     |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                      |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.05x slower                                                     |
| coverage                 | 79.4 ms                                                | 86.1 ms: 1.08x slower                                                     |
| telco                    | 7.27 ms                                                | 8.00 ms: 1.10x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 6.78 ms: 1.14x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 80.2 ms: 3.34x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241106-3.14.0a1+-3c18fc8/bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.446x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.25x