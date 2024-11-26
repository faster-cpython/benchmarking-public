# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_16384
- machine: linux-x86_64
- commit hash: 5092a50
- commit date: 2024-11-21
- overall geometric mean: 1.414x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                      |
| docutils       | 3.30 sec                                               | 2.75 sec: 1.20x faster                                                    |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 909 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.4 ms: 1.84x faster                                                     |
| float          | 117 ms                                                 | 78.9 ms: 1.48x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.41x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                     |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                     |
| json_loads           | 31.2 us                                                | 26.3 us: 1.19x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                     |
| django_template | 48.2 ms                                                | 33.4 ms: 1.44x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.50x faster                                                     |
| generators               | 80.1 ms                                                | 35.2 ms: 2.27x faster                                                     |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                                      |
| pylint                   | 551 ms                                                 | 268 ms: 2.06x faster                                                      |
| richards_super           | 94.7 ms                                                | 46.2 ms: 2.05x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                     |
| richards                 | 79.3 ms                                                | 40.2 ms: 1.97x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 909 ms: 1.95x faster                                                      |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                     |
| logging_silent           | 190 ns                                                 | 98.9 ns: 1.92x faster                                                     |
| go                       | 240 ms                                                 | 126 ms: 1.90x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                                     |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                      |
| nbody                    | 154 ms                                                 | 83.4 ms: 1.84x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 64.8 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                      |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                                      |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                      |
| djangocms                | 38.4 us                                                | 22.0 us: 1.75x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                     |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.59x faster                                                     |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                      |
| pyflate                  | 716 ms                                                 | 452 ms: 1.58x faster                                                      |
| comprehensions           | 28.8 us                                                | 18.2 us: 1.58x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.73 ms: 1.55x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                     |
| float                    | 117 ms                                                 | 78.9 ms: 1.48x faster                                                     |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.45x faster                                                      |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                      |
| django_template          | 48.2 ms                                                | 33.4 ms: 1.44x faster                                                     |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.43x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 727 ms: 1.40x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.64 ms: 1.40x faster                                                     |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                      |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.36x faster                                                     |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                     |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                      |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.28x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 55.3 ms: 1.25x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 67.5 ms: 1.25x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                     |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                      |
| nqueens                  | 106 ms                                                 | 87.8 ms: 1.21x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.75 sec: 1.20x faster                                                    |
| json_loads               | 31.2 us                                                | 26.3 us: 1.19x faster                                                     |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                      |
| json                     | 5.69 ms                                                | 4.81 ms: 1.18x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.03x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                      |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                      |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.49 ms: 1.03x slower                                                     |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.68 ms: 1.29x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                              |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241121-3.14.0a2+-5092a50-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.414x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x