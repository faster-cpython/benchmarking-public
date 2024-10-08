# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed_8
- machine: linux-x86_64
- commit hash: 95535e9
- commit date: 2024-07-13
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                        |
| docutils       | 3.30 sec                                               | 3.02 sec: 1.09x faster                                                      |
| html5lib       | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                       |
| tornado_http   | 136 ms                                                 | 93.6 ms: 1.46x faster                                                       |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.7 ms: 1.93x faster                                                       |
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                       |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 3.88 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                        |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                       |
| django_template | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 56.6 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                                        |
| generators               | 80.1 ms                                                | 30.8 ms: 2.60x faster                                                       |
| richards_super           | 94.7 ms                                                | 41.1 ms: 2.31x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.31x faster                                                       |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                        |
| richards                 | 79.3 ms                                                | 36.3 ms: 2.18x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.15x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                                        |
| chaos                    | 115 ms                                                 | 57.1 ms: 2.02x faster                                                       |
| nbody                    | 154 ms                                                 | 79.7 ms: 1.93x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 62.0 ms: 1.91x faster                                                       |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                        |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                        |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                                        |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                       |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                      |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                       |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                        |
| pyflate                  | 716 ms                                                 | 449 ms: 1.59x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                       |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                        |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.49x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                       |
| pylint                   | 551 ms                                                 | 373 ms: 1.48x faster                                                        |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                        |
| fannkuch                 | 532 ms                                                 | 361 ms: 1.47x faster                                                        |
| tornado_http             | 136 ms                                                 | 93.6 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| django_template          | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 742 ms: 1.37x faster                                                        |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                        |
| html5lib                 | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                      |
| thrift                   | 1.07 ms                                                | 807 us: 1.33x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                       |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 66.6 ms: 1.27x faster                                                       |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                        |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                       |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 57.4 ms: 1.20x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 826 us: 1.19x faster                                                        |
| sympy_str                | 346 ms                                                 | 290 ms: 1.19x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 21.9 ms: 1.18x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                       |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 56.6 ms: 1.17x faster                                                       |
| sympy_expand             | 566 ms                                                 | 493 ms: 1.15x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| json                     | 5.69 ms                                                | 5.20 ms: 1.10x faster                                                       |
| docutils                 | 3.30 sec                                               | 3.02 sec: 1.09x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.58 ms: 1.01x faster                                                       |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                                        |
| async_generators         | 444 ms                                                 | 449 ms: 1.01x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.88 ms: 1.07x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                       |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                       |
| coverage                 | 79.4 ms                                                | 92.2 ms: 1.16x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-95535e9-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x