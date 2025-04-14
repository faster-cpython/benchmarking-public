# Results vs. 3.10.4

- fork: python
- ref: 05a370abd6cdfe4b54be
- machine: linux-x86_64
- commit hash: 05a370a
- commit date: 2023-12-01
- overall geometric mean: 1.359x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                                   |
| chameleon      | 9.68 ms                                                | 6.94 ms: 1.39x faster                                                  |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.36x faster                                                  |
| tornado_http   | 136 ms                                                 | 95.9 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 472 ms: 1.54x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 571 ms: 1.52x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 740 ms: 1.37x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.48x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| float          | 117 ms                                                 | 82.5 ms: 1.42x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.14x faster                                                  |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.20 sec: 1.43x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 87.3 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 109 ms: 1.05x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 9.03 ms: 1.52x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 51.9 ms: 1.27x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 115 us: 4.71x faster                                                   |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                                  |
| chaos                    | 115 ms                                                 | 60.7 ms: 1.90x faster                                                  |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                   |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                   |
| pylint                   | 551 ms                                                 | 306 ms: 1.80x faster                                                   |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 71.3 ms: 1.79x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                  |
| richards_super           | 94.7 ms                                                | 54.4 ms: 1.74x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                  |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                                  |
| nbody                    | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| richards                 | 79.3 ms                                                | 48.8 ms: 1.63x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.1 ms: 1.58x faster                                                  |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                   |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                   |
| async_tree_none          | 728 ms                                                 | 472 ms: 1.54x faster                                                   |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 571 ms: 1.52x faster                                                   |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 38.7 us: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                 |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.20 sec: 1.43x faster                                                 |
| logging_format           | 9.09 us                                                | 6.36 us: 1.43x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.83 us: 1.42x faster                                                  |
| tornado_http             | 136 ms                                                 | 95.9 ms: 1.42x faster                                                  |
| float                    | 117 ms                                                 | 82.5 ms: 1.42x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                 |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                   |
| chameleon                | 9.68 ms                                                | 6.94 ms: 1.39x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.38x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 740 ms: 1.37x faster                                                   |
| fannkuch                 | 532 ms                                                 | 388 ms: 1.37x faster                                                   |
| deepcopy                 | 479 us                                                 | 349 us: 1.37x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.36x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                   |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.12 us: 1.34x faster                                                  |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.33x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                                   |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 51.9 ms: 1.27x faster                                                  |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 66.6 ms: 1.27x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.13 ms: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 137 ms: 1.26x faster                                                   |
| gunicorn                 | 1.53 ms                                                | 1.25 ms: 1.23x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 846 us: 1.17x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 87.3 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.14x faster                                                  |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.11x faster                                                 |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                  |
| pathlib                  | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 109 ms: 1.05x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                   |
| async_generators         | 444 ms                                                 | 451 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 8.46 ms: 1.16x slower                                                  |
| coverage                 | 79.4 ms                                                | 95.6 ms: 1.20x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.01 ms: 1.38x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.03 ms: 1.52x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                           |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20231201-3.13.0a2+-05a370a/bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.359x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.23x