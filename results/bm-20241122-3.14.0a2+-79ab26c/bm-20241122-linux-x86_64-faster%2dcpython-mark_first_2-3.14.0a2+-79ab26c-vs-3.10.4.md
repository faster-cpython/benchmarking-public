# Results vs. 3.10.4

- fork: faster-cpython
- ref: mark_first_2
- machine: linux-x86_64
- commit hash: 79ab26c
- commit date: 2024-11-22
- overall geometric mean: 1.429x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                     |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                   |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 628 ms: 2.82x faster                                                     |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.68x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 340 ms: 2.56x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.52x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.6 ms: 1.64x faster                                                    |
| float          | 117 ms                                                 | 76.8 ms: 1.52x faster                                                    |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| regex_v8       | 27.8 ms                                                | 26.8 ms: 1.04x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 97.7 ms: 1.18x faster                                                    |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                    |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                    |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                     |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 628 ms: 2.82x faster                                                     |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.68x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 340 ms: 2.56x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                     |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                     |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                    |
| chaos                    | 115 ms                                                 | 60.8 ms: 1.90x faster                                                    |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                     |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                     |
| richards_super           | 94.7 ms                                                | 52.6 ms: 1.80x faster                                                    |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 71.8 ms: 1.78x faster                                                    |
| djangocms                | 38.4 us                                                | 21.6 us: 1.78x faster                                                    |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.72x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 69.1 ms: 1.71x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                    |
| richards                 | 79.3 ms                                                | 46.6 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                    |
| nbody                    | 154 ms                                                 | 93.6 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                    |
| pyflate                  | 716 ms                                                 | 465 ms: 1.54x faster                                                     |
| float                    | 117 ms                                                 | 76.8 ms: 1.52x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                     |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                     |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                    |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                    |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.2 ms: 1.44x faster                                                    |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                    |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                    |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                     |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.35x faster                                                     |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                     |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.32x faster                                                     |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.31x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 64.9 ms: 1.30x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                    |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                   |
| scimark_fft              | 466 ms                                                 | 370 ms: 1.26x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                    |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 97.7 ms: 1.18x faster                                                    |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 851 us: 1.16x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                    |
| json                     | 5.69 ms                                                | 4.99 ms: 1.14x faster                                                    |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                    |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.8 ms: 1.04x faster                                                    |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                     |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                    |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.36x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 80.8 ms: 3.36x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                             |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241122-3.14.0a2+-79ab26c/bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.429x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.26x