# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 190fbfa
- commit date: 2024-07-14
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                      |
| docutils       | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                    |
| html5lib       | 88.9 ms                                                | 71.6 ms: 1.24x faster                                                     |
| tornado_http   | 136 ms                                                 | 98.3 ms: 1.39x faster                                                     |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 910 ms: 1.94x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 77.0 ms: 1.99x faster                                                     |
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                     |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.50x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                     |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.53x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.96 ms: 1.64x faster                                                     |
| django_template | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                     |
| genshi_text     | 31.8 ms                                                | 27.7 ms: 1.15x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 63.3 ms: 1.04x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.42 ms: 2.31x faster                                                     |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.6 us: 2.20x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                                      |
| richards_super           | 94.7 ms                                                | 45.3 ms: 2.09x faster                                                     |
| chaos                    | 115 ms                                                 | 56.0 ms: 2.06x faster                                                     |
| richards                 | 79.3 ms                                                | 39.1 ms: 2.03x faster                                                     |
| nbody                    | 154 ms                                                 | 77.0 ms: 1.99x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 910 ms: 1.94x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                     |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 63.4 ms: 1.86x faster                                                     |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                      |
| deepcopy                 | 479 us                                                 | 258 us: 1.85x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 518 ms: 1.78x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                     |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.74x faster                                                      |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                     |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                      |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                     |
| mako                     | 16.3 ms                                                | 9.96 ms: 1.64x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.60x faster                                                     |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.53x faster                                                      |
| pylint                   | 551 ms                                                 | 368 ms: 1.50x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                     |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                     |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                                     |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                      |
| fannkuch                 | 532 ms                                                 | 366 ms: 1.45x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                    |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                      |
| generators               | 80.1 ms                                                | 56.1 ms: 1.43x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                    |
| tornado_http             | 136 ms                                                 | 98.3 ms: 1.39x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                     |
| thrift                   | 1.07 ms                                                | 807 us: 1.33x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                     |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                      |
| coroutines               | 35.1 ms                                                | 27.6 ms: 1.27x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 66.7 ms: 1.26x faster                                                     |
| html5lib                 | 88.9 ms                                                | 71.6 ms: 1.24x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 57.3 ms: 1.21x faster                                                     |
| django_template          | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                     |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                      |
| sympy_expand             | 566 ms                                                 | 489 ms: 1.16x faster                                                      |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 857 us: 1.15x faster                                                      |
| genshi_text              | 31.8 ms                                                | 27.7 ms: 1.15x faster                                                     |
| dask                     | 441 ms                                                 | 384 ms: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                    |
| nqueens                  | 106 ms                                                 | 97.5 ms: 1.09x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 63.3 ms: 1.04x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 25.3 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                     |
| telco                    | 7.27 ms                                                | 8.00 ms: 1.10x slower                                                     |
| async_generators         | 444 ms                                                 | 514 ms: 1.16x slower                                                      |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                              |

Benchmark hidden because not significant (3): regex_effbot, asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-190fbfa-JIT/bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.18x