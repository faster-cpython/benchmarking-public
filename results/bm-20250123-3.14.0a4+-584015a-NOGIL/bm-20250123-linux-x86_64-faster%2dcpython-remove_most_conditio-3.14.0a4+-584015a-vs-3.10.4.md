# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 584015a
- commit date: 2025-01-23
- overall geometric mean: 1.226x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 313 ms: 1.11x faster                                                             |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                           |
| html5lib       | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                            |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| async_tree_none         | 728 ms                                                 | 294 ms: 2.48x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 373 ms: 2.33x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 532 ms: 1.91x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.37x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 78.6 ms: 1.49x faster                                                            |
| nbody          | 154 ms                                                 | 137 ms: 1.12x faster                                                             |
| pidigits       | 191 ms                                                 | 182 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 152 ms: 1.24x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.43 sec: 1.29x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 377 us: 1.28x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 261 us: 1.27x faster                                                             |
| xml_etree_iterparse  | 115 ms                                                 | 95.9 ms: 1.20x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 68.6 ms: 1.15x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                             |
| json_dumps           | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 96.2 ms: 1.03x faster                                                            |
| json_loads           | 31.2 us                                                | 31.4 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.1 ms: 1.03x slower                                                            |
| python_startup_no_site | 5.93 ms                                                | 9.37 ms: 1.58x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 42.9 ms: 1.12x faster                                                            |
| genshi_text     | 31.8 ms                                                | 29.0 ms: 1.10x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 62.0 ms: 1.07x faster                                                            |
| mako            | 16.3 ms                                                | 16.7 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| typing_runtime_protocols | 544 us                                                 | 213 us: 2.55x faster                                                             |
| generators               | 80.1 ms                                                | 32.0 ms: 2.50x faster                                                            |
| async_tree_none          | 728 ms                                                 | 294 ms: 2.48x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 373 ms: 2.33x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 532 ms: 1.91x faster                                                             |
| pylint                   | 551 ms                                                 | 323 ms: 1.71x faster                                                             |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                             |
| deltablue                | 7.91 ms                                                | 4.84 ms: 1.63x faster                                                            |
| logging_silent           | 190 ns                                                 | 122 ns: 1.55x faster                                                             |
| chaos                    | 115 ms                                                 | 75.2 ms: 1.54x faster                                                            |
| scimark_sor              | 220 ms                                                 | 144 ms: 1.52x faster                                                             |
| deepcopy                 | 479 us                                                 | 315 us: 1.52x faster                                                             |
| float                    | 117 ms                                                 | 78.6 ms: 1.49x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 40.0 us: 1.46x faster                                                            |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.45x faster                                                             |
| raytrace                 | 507 ms                                                 | 359 ms: 1.41x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 90.7 ms: 1.41x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.58 ms: 1.37x faster                                                            |
| comprehensions           | 28.8 us                                                | 21.0 us: 1.37x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 87.3 ms: 1.35x faster                                                            |
| coroutines               | 35.1 ms                                                | 25.9 ms: 1.35x faster                                                            |
| pyflate                  | 716 ms                                                 | 537 ms: 1.33x faster                                                             |
| richards_super           | 94.7 ms                                                | 71.8 ms: 1.32x faster                                                            |
| hexiom                   | 10.4 ms                                                | 7.89 ms: 1.32x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.98 ms: 1.30x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.43 sec: 1.29x faster                                                           |
| html5lib                 | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 377 us: 1.28x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                                           |
| richards                 | 79.3 ms                                                | 62.4 ms: 1.27x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 261 us: 1.27x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                            |
| scimark_lu               | 176 ms                                                 | 142 ms: 1.24x faster                                                             |
| regex_compile            | 188 ms                                                 | 152 ms: 1.24x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 69.3 ms: 1.22x faster                                                            |
| logging_simple           | 8.30 us                                                | 6.83 us: 1.22x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 95.9 ms: 1.20x faster                                                            |
| logging_format           | 9.09 us                                                | 7.64 us: 1.19x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 867 ms: 1.17x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.79 sec: 1.17x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 123 ms: 1.16x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 68.6 ms: 1.15x faster                                                            |
| thrift                   | 1.07 ms                                                | 943 us: 1.14x faster                                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.6 ms: 1.14x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 61.5 ms: 1.12x faster                                                            |
| django_template          | 48.2 ms                                                | 42.9 ms: 1.12x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                             |
| nbody                    | 154 ms                                                 | 137 ms: 1.12x faster                                                             |
| 2to3                     | 348 ms                                                 | 313 ms: 1.11x faster                                                             |
| json_dumps               | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                            |
| scimark_fft              | 466 ms                                                 | 421 ms: 1.11x faster                                                             |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                            |
| genshi_text              | 31.8 ms                                                | 29.0 ms: 1.10x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| sympy_str                | 346 ms                                                 | 321 ms: 1.08x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 24.2 ms: 1.07x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 62.0 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.13 ms: 1.06x faster                                                            |
| sympy_expand             | 566 ms                                                 | 538 ms: 1.05x faster                                                             |
| pidigits                 | 191 ms                                                 | 182 ms: 1.05x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 164 ms: 1.05x faster                                                             |
| nqueens                  | 106 ms                                                 | 101 ms: 1.05x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 96.2 ms: 1.03x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.76 sec: 1.03x faster                                                           |
| fannkuch                 | 532 ms                                                 | 522 ms: 1.02x faster                                                             |
| json                     | 5.69 ms                                                | 5.58 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                             |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                                             |
| json_loads               | 31.2 us                                                | 31.4 us: 1.01x slower                                                            |
| mako                     | 16.3 ms                                                | 16.7 ms: 1.02x slower                                                            |
| python_startup           | 14.6 ms                                                | 15.1 ms: 1.03x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                            |
| meteor_contest           | 120 ms                                                 | 134 ms: 1.12x slower                                                             |
| gc_traversal             | 3.62 ms                                                | 4.44 ms: 1.22x slower                                                            |
| telco                    | 7.27 ms                                                | 9.14 ms: 1.26x slower                                                            |
| coverage                 | 79.4 ms                                                | 107 ms: 1.35x slower                                                             |
| python_startup_no_site   | 5.93 ms                                                | 9.37 ms: 1.58x slower                                                            |
| bench_thread_pool        | 986 us                                                 | 3.47 ms: 3.52x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 90.0 ms: 3.75x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250123-3.14.0a4+-584015a-NOGIL/bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.226x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.51x