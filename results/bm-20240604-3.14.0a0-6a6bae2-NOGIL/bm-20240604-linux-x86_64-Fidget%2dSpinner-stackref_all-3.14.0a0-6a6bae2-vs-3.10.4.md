# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 406 ms: 1.17x slower                                                    |
| docutils       | 3.30 sec                                               | 3.44 sec: 1.04x slower                                                  |
| html5lib       | 88.9 ms                                                | 102 ms: 1.14x slower                                                    |
| tornado_http   | 136 ms                                                 | 139 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 979 ms: 1.81x faster                                                    |
| async_tree_none         | 728 ms                                                 | 472 ms: 1.54x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 586 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 732 ms: 1.39x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.55x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| float          | 117 ms                                                 | 141 ms: 1.20x slower                                                    |
| nbody          | 154 ms                                                 | 234 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                  | 1.22x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                   |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                    |
| regex_compile  | 188 ms                                                 | 227 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                    |
| pickle_list          | 5.08 us                                                | 4.90 us: 1.04x faster                                                   |
| json_dumps           | 14.2 ms                                                | 14.2 ms: 1.00x slower                                                   |
| json_loads           | 31.2 us                                                | 31.8 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 118 ms: 1.02x slower                                                    |
| tomli_loads          | 3.14 sec                                               | 3.38 sec: 1.08x slower                                                  |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                   |
| unpickle_list        | 5.20 us                                                | 5.73 us: 1.10x slower                                                   |
| unpickle             | 14.4 us                                                | 16.2 us: 1.13x slower                                                   |
| xml_etree_generate   | 99.4 ms                                                | 115 ms: 1.15x slower                                                    |
| xml_etree_process    | 79.1 ms                                                | 92.8 ms: 1.17x slower                                                   |
| pickle_pure_python   | 484 us                                                 | 611 us: 1.26x slower                                                    |
| unpickle_pure_python | 331 us                                                 | 423 us: 1.28x slower                                                    |
| pickle_dict          | 29.6 us                                                | 41.1 us: 1.39x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.7 ms: 1.07x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 9.18 ms: 1.55x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 62.9 ms: 1.31x slower                                                   |
| genshi_text     | 31.8 ms                                                | 41.6 ms: 1.31x slower                                                   |
| genshi_xml      | 66.0 ms                                                | 86.7 ms: 1.31x slower                                                   |
| mako            | 16.3 ms                                                | 21.6 ms: 1.32x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.31x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| generators               | 80.1 ms                                                | 39.1 ms: 2.05x faster                                                   |
| typing_runtime_protocols | 544 us                                                 | 266 us: 2.04x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 979 ms: 1.81x faster                                                    |
| async_tree_none          | 728 ms                                                 | 472 ms: 1.54x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 600 ms: 1.54x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 586 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 732 ms: 1.39x faster                                                    |
| pylint                   | 551 ms                                                 | 405 ms: 1.36x faster                                                    |
| gc_traversal             | 3.62 ms                                                | 2.78 ms: 1.30x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.13 sec: 1.21x faster                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.37 ms: 1.18x faster                                                   |
| bench_mp_pool            | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 117 ms: 1.09x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.7 ms: 1.07x faster                                                   |
| coroutines               | 35.1 ms                                                | 33.0 ms: 1.06x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                   |
| pathlib                  | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                   |
| pickle_list              | 5.08 us                                                | 4.90 us: 1.04x faster                                                   |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                    |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| json_dumps               | 14.2 ms                                                | 14.2 ms: 1.00x slower                                                   |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                    |
| json_loads               | 31.2 us                                                | 31.8 us: 1.02x slower                                                   |
| tornado_http             | 136 ms                                                 | 139 ms: 1.02x slower                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 118 ms: 1.02x slower                                                    |
| comprehensions           | 28.8 us                                                | 29.7 us: 1.03x slower                                                   |
| docutils                 | 3.30 sec                                               | 3.44 sec: 1.04x slower                                                  |
| pycparser                | 1.58 sec                                               | 1.65 sec: 1.05x slower                                                  |
| json                     | 5.69 ms                                                | 5.98 ms: 1.05x slower                                                   |
| richards                 | 79.3 ms                                                | 83.6 ms: 1.05x slower                                                   |
| dulwich_log              | 84.3 ms                                                | 89.0 ms: 1.06x slower                                                   |
| richards_super           | 94.7 ms                                                | 101 ms: 1.06x slower                                                    |
| logging_silent           | 190 ns                                                 | 203 ns: 1.07x slower                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.94 ms: 1.07x slower                                                   |
| sqlite_synth             | 3.02 us                                                | 3.25 us: 1.07x slower                                                   |
| tomli_loads              | 3.14 sec                                               | 3.38 sec: 1.08x slower                                                  |
| scimark_fft              | 466 ms                                                 | 506 ms: 1.09x slower                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 130 ms: 1.10x slower                                                    |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.73 us: 1.10x slower                                                   |
| deltablue                | 7.91 ms                                                | 8.80 ms: 1.11x slower                                                   |
| chaos                    | 115 ms                                                 | 129 ms: 1.12x slower                                                    |
| unpickle                 | 14.4 us                                                | 16.2 us: 1.13x slower                                                   |
| pyflate                  | 716 ms                                                 | 813 ms: 1.14x slower                                                    |
| html5lib                 | 88.9 ms                                                | 102 ms: 1.14x slower                                                    |
| sympy_integrate          | 25.8 ms                                                | 29.5 ms: 1.14x slower                                                   |
| spectral_norm            | 170 ms                                                 | 195 ms: 1.15x slower                                                    |
| nqueens                  | 106 ms                                                 | 122 ms: 1.15x slower                                                    |
| xml_etree_generate       | 99.4 ms                                                | 115 ms: 1.15x slower                                                    |
| 2to3                     | 348 ms                                                 | 406 ms: 1.17x slower                                                    |
| xml_etree_process        | 79.1 ms                                                | 92.8 ms: 1.17x slower                                                   |
| fannkuch                 | 532 ms                                                 | 626 ms: 1.18x slower                                                    |
| deepcopy_memo            | 58.5 us                                                | 69.8 us: 1.19x slower                                                   |
| float                    | 117 ms                                                 | 141 ms: 1.20x slower                                                    |
| mdp                      | 2.85 sec                                               | 3.42 sec: 1.20x slower                                                  |
| regex_compile            | 188 ms                                                 | 227 ms: 1.21x slower                                                    |
| hexiom                   | 10.4 ms                                                | 12.7 ms: 1.22x slower                                                   |
| raytrace                 | 507 ms                                                 | 628 ms: 1.24x slower                                                    |
| scimark_sor              | 220 ms                                                 | 274 ms: 1.25x slower                                                    |
| deepcopy                 | 479 us                                                 | 598 us: 1.25x slower                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 3.22 ms: 1.25x slower                                                   |
| pickle_pure_python       | 484 us                                                 | 611 us: 1.26x slower                                                    |
| sqlglot_parse            | 2.17 ms                                                | 2.74 ms: 1.26x slower                                                   |
| sympy_str                | 346 ms                                                 | 438 ms: 1.27x slower                                                    |
| sqlglot_normalize        | 143 ms                                                 | 182 ms: 1.27x slower                                                    |
| async_generators         | 444 ms                                                 | 565 ms: 1.27x slower                                                    |
| unpickle_pure_python     | 331 us                                                 | 423 us: 1.28x slower                                                    |
| meteor_contest           | 120 ms                                                 | 154 ms: 1.29x slower                                                    |
| deepcopy_reduce          | 4.17 us                                                | 5.39 us: 1.29x slower                                                   |
| django_template          | 48.2 ms                                                | 62.9 ms: 1.31x slower                                                   |
| genshi_text              | 31.8 ms                                                | 41.6 ms: 1.31x slower                                                   |
| genshi_xml               | 66.0 ms                                                | 86.7 ms: 1.31x slower                                                   |
| mako                     | 16.3 ms                                                | 21.6 ms: 1.32x slower                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 91.4 ms: 1.32x slower                                                   |
| logging_simple           | 8.30 us                                                | 11.1 us: 1.33x slower                                                   |
| sympy_sum                | 196 ms                                                 | 262 ms: 1.33x slower                                                    |
| logging_format           | 9.09 us                                                | 12.2 us: 1.34x slower                                                   |
| pprint_pformat           | 2.10 sec                                               | 2.85 sec: 1.35x slower                                                  |
| telco                    | 7.27 ms                                                | 9.83 ms: 1.35x slower                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 1.38 sec: 1.35x slower                                                  |
| go                       | 240 ms                                                 | 329 ms: 1.37x slower                                                    |
| sympy_expand             | 566 ms                                                 | 778 ms: 1.37x slower                                                    |
| pickle_dict              | 29.6 us                                                | 41.1 us: 1.39x slower                                                   |
| scimark_lu               | 176 ms                                                 | 254 ms: 1.44x slower                                                    |
| nbody                    | 154 ms                                                 | 234 ms: 1.53x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 9.18 ms: 1.55x slower                                                   |
| bench_thread_pool        | 986 us                                                 | 3.15 ms: 3.19x slower                                                   |
| coverage                 | 79.4 ms                                                | 802 ms: 10.10x slower                                                   |
| thrift                   | 1.07 ms                                                | 13.6 ms: 12.69x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.15x slower                                                            |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.14.0a0-6a6bae2-NOGIL/bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.28x