# Results vs. 3.10.4

- fork: brandtbucher
- ref: peel
- machine: linux-x86_64
- commit hash: ee3b5e3
- commit date: 2024-05-10
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                        |
| chameleon      | 9.68 ms                                                | 6.97 ms: 1.39x faster                                       |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.32x faster                                       |
| tornado_http   | 136 ms                                                 | 97.5 ms: 1.40x faster                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 364 ms: 2.00x faster                                        |
| async_tree_io           | 1.77 sec                                               | 954 ms: 1.85x faster                                        |
| async_tree_memoization  | 870 ms                                                 | 478 ms: 1.82x faster                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 624 ms: 1.63x faster                                        |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.9 ms: 1.83x faster                                       |
| float          | 117 ms                                                 | 71.2 ms: 1.64x faster                                       |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.45x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                        |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                       |
| regex_effbot   | 3.63 ms                                                | 3.51 ms: 1.03x faster                                       |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                      |
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                        |
| unpickle_pure_python | 331 us                                                 | 227 us: 1.46x faster                                        |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                       |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                       |
| xml_etree_generate   | 99.4 ms                                                | 83.3 ms: 1.19x faster                                       |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.11x faster                                        |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.52 us: 1.06x slower                                       |
| unpickle             | 14.4 us                                                | 15.6 us: 1.09x slower                                       |
| pickle_list          | 5.08 us                                                | 5.60 us: 1.10x slower                                       |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                       |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                       |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                       |
| python_startup_no_site | 5.93 ms                                                | 7.60 ms: 1.28x slower                                       |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.59 ms: 1.70x faster                                       |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                       |
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                       |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.14x faster                                       |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                        |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                       |
| deltablue                | 7.91 ms                                                | 3.72 ms: 2.13x faster                                       |
| async_tree_none          | 728 ms                                                 | 364 ms: 2.00x faster                                        |
| richards_super           | 94.7 ms                                                | 47.7 ms: 1.99x faster                                       |
| richards                 | 79.3 ms                                                | 41.5 ms: 1.91x faster                                       |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 68.2 ms: 1.87x faster                                       |
| async_tree_io            | 1.77 sec                                               | 954 ms: 1.85x faster                                        |
| nbody                    | 154 ms                                                 | 83.9 ms: 1.83x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 478 ms: 1.82x faster                                        |
| raytrace                 | 507 ms                                                 | 281 ms: 1.81x faster                                        |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                        |
| asyncio_tcp              | 922 ms                                                 | 520 ms: 1.77x faster                                        |
| spectral_norm            | 170 ms                                                 | 97.1 ms: 1.75x faster                                       |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                       |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                        |
| mako                     | 16.3 ms                                                | 9.59 ms: 1.70x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                       |
| float                    | 117 ms                                                 | 71.2 ms: 1.64x faster                                       |
| go                       | 240 ms                                                 | 147 ms: 1.64x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 624 ms: 1.63x faster                                        |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                      |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                        |
| pyflate                  | 716 ms                                                 | 449 ms: 1.59x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                       |
| pylint                   | 551 ms                                                 | 356 ms: 1.55x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 37.8 us: 1.55x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.80 ms: 1.53x faster                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                       |
| fannkuch                 | 532 ms                                                 | 359 ms: 1.48x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 227 us: 1.46x faster                                        |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                        |
| scimark_lu               | 176 ms                                                 | 122 ms: 1.44x faster                                        |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.58 ms: 1.41x faster                                       |
| tornado_http             | 136 ms                                                 | 97.5 ms: 1.40x faster                                       |
| logging_format           | 9.09 us                                                | 6.50 us: 1.40x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                        |
| chameleon                | 9.68 ms                                                | 6.97 ms: 1.39x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                      |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                       |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                       |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                       |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                       |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.32x faster                                       |
| thrift                   | 1.07 ms                                                | 833 us: 1.29x faster                                        |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                       |
| deepcopy                 | 479 us                                                 | 381 us: 1.26x faster                                        |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                        |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.35 us: 1.24x faster                                       |
| nqueens                  | 106 ms                                                 | 85.9 ms: 1.23x faster                                       |
| dulwich_log              | 84.3 ms                                                | 68.8 ms: 1.23x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 57.2 ms: 1.21x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 83.3 ms: 1.19x faster                                       |
| dask                     | 441 ms                                                 | 380 ms: 1.16x faster                                        |
| pathlib                  | 20.5 ms                                                | 17.7 ms: 1.16x faster                                       |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.14x faster                                       |
| sympy_str                | 346 ms                                                 | 305 ms: 1.14x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                        |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 22.9 ms: 1.13x faster                                       |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.11x faster                                        |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                        |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                      |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                       |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                       |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                       |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                       |
| regex_effbot             | 3.63 ms                                                | 3.51 ms: 1.03x faster                                       |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                        |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                        |
| asyncio_websockets       | 559 ms                                                 | 568 ms: 1.02x slower                                        |
| async_generators         | 444 ms                                                 | 469 ms: 1.06x slower                                        |
| unpickle_list            | 5.20 us                                                | 5.52 us: 1.06x slower                                       |
| gc_traversal             | 3.62 ms                                                | 3.90 ms: 1.08x slower                                       |
| flaskblogging            | 8.58 ms                                                | 9.27 ms: 1.08x slower                                       |
| unpickle                 | 14.4 us                                                | 15.6 us: 1.09x slower                                       |
| pickle_list              | 5.08 us                                                | 5.60 us: 1.10x slower                                       |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.84 ms: 1.14x slower                                       |
| coverage                 | 79.4 ms                                                | 92.0 ms: 1.16x slower                                       |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.60 ms: 1.28x slower                                       |
| telco                    | 7.27 ms                                                | 172 ms: 23.69x slower                                       |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240510-3.14.0a0-ee3b5e3-JIT/bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.22x