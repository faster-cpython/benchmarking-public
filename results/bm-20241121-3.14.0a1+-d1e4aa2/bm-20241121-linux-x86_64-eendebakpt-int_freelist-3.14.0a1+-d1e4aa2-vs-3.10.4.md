# Results vs. 3.10.4

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.410x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                               |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                             |
| html5lib       | 88.9 ms                                                | 63.6 ms: 1.40x faster                                              |
| Geometric mean | (ref)                                                  | 1.32x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                               |
| async_tree_io           | 1.77 sec                                               | 847 ms: 2.09x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                               |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.4 ms: 1.63x faster                                              |
| float          | 117 ms                                                 | 79.1 ms: 1.48x faster                                              |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                               |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                              |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.16x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.56x faster                                             |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                               |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 85.9 ms: 1.16x faster                                              |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                               |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                              |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                              |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.31x faster                                              |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                               |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                              |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                              |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                               |
| async_tree_io            | 1.77 sec                                               | 847 ms: 2.09x faster                                               |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.90x faster                                              |
| chaos                    | 115 ms                                                 | 60.9 ms: 1.90x faster                                              |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                               |
| raytrace                 | 507 ms                                                 | 275 ms: 1.85x faster                                               |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                               |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                               |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                              |
| djangocms                | 38.4 us                                                | 21.8 us: 1.76x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                              |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                               |
| richards                 | 79.3 ms                                                | 46.9 ms: 1.69x faster                                              |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                              |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                              |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                               |
| nbody                    | 154 ms                                                 | 94.4 ms: 1.63x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                              |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                               |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.56x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                               |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                              |
| float                    | 117 ms                                                 | 79.1 ms: 1.48x faster                                              |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                               |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                               |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                              |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                              |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                              |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                              |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                              |
| html5lib                 | 88.9 ms                                                | 63.6 ms: 1.40x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                              |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                              |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                               |
| scimark_fft              | 466 ms                                                 | 345 ms: 1.35x faster                                               |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.34x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                               |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                              |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.31x faster                                              |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                              |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                              |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                              |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                               |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 85.9 ms: 1.16x faster                                              |
| bench_thread_pool        | 986 us                                                 | 856 us: 1.15x faster                                               |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                              |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                              |
| json                     | 5.69 ms                                                | 5.00 ms: 1.14x faster                                              |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                               |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                              |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                               |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                               |
| coverage                 | 79.4 ms                                                | 83.9 ms: 1.06x slower                                              |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.67x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 79.1 ms: 3.29x slower                                              |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                       |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.410x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.26x