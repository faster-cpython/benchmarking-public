# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                |
| chameleon      | 9.68 ms                                                | 7.07 ms: 1.37x faster                                               |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                              |
| html5lib       | 88.9 ms                                                | 68.0 ms: 1.31x faster                                               |
| tornado_http   | 136 ms                                                 | 96.8 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                  | 1.28x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 386 ms: 1.89x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 464 ms: 1.87x faster                                                |
| async_tree_io           | 1.77 sec                                               | 959 ms: 1.84x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 619 ms: 1.64x faster                                                |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.3 ms: 1.91x faster                                               |
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                               |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.47x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                               |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                                |
| regex_effbot   | 3.63 ms                                                | 3.94 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                              |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 82.8 ms: 1.20x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.11x faster                                                |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                               |
| unpickle_list        | 5.20 us                                                | 5.28 us: 1.02x slower                                               |
| unpickle             | 14.4 us                                                | 15.8 us: 1.10x slower                                               |
| pickle               | 10.7 us                                                | 11.8 us: 1.10x slower                                               |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.61 ms: 1.28x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.00 ms: 1.63x faster                                              |
| django_template | 48.2 ms                                                | 36.9 ms: 1.31x faster                                               |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.30x faster                                               |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.13x faster                                               |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                |
| generators               | 80.1 ms                                                | 30.9 ms: 2.59x faster                                               |
| deltablue                | 7.91 ms                                                | 3.73 ms: 2.12x faster                                               |
| richards_super           | 94.7 ms                                                | 47.3 ms: 2.00x faster                                               |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                               |
| nbody                    | 154 ms                                                 | 80.3 ms: 1.91x faster                                               |
| richards                 | 79.3 ms                                                | 41.6 ms: 1.91x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 62.1 ms: 1.90x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                               |
| async_tree_none          | 728 ms                                                 | 386 ms: 1.89x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 464 ms: 1.87x faster                                                |
| async_tree_io            | 1.77 sec                                               | 959 ms: 1.84x faster                                                |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.77x faster                                                |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                               |
| spectral_norm            | 170 ms                                                 | 99.5 ms: 1.71x faster                                               |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 619 ms: 1.64x faster                                                |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                |
| mako                     | 16.3 ms                                                | 10.00 ms: 1.63x faster                                              |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                               |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 38.3 us: 1.53x faster                                               |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                               |
| fannkuch                 | 532 ms                                                 | 350 ms: 1.52x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.59 ms: 1.41x faster                                               |
| tornado_http             | 136 ms                                                 | 96.8 ms: 1.41x faster                                               |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                              |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                               |
| chameleon                | 9.68 ms                                                | 7.07 ms: 1.37x faster                                               |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                               |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                               |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                              |
| html5lib                 | 88.9 ms                                                | 68.0 ms: 1.31x faster                                               |
| django_template          | 48.2 ms                                                | 36.9 ms: 1.31x faster                                               |
| thrift                   | 1.07 ms                                                | 824 us: 1.30x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.30x faster                                               |
| deepcopy                 | 479 us                                                 | 372 us: 1.29x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 3.31 us: 1.26x faster                                               |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                |
| nqueens                  | 106 ms                                                 | 85.4 ms: 1.24x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                               |
| dulwich_log              | 84.3 ms                                                | 69.1 ms: 1.22x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 82.8 ms: 1.20x faster                                               |
| dask                     | 441 ms                                                 | 377 ms: 1.17x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                               |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                |
| bench_thread_pool        | 986 us                                                 | 864 us: 1.14x faster                                                |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.13x faster                                               |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.11x faster                                                |
| sympy_expand             | 566 ms                                                 | 509 ms: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                              |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                               |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                               |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                               |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                                |
| unpickle_list            | 5.20 us                                                | 5.28 us: 1.02x slower                                               |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.86 ms: 1.06x slower                                               |
| flaskblogging            | 8.58 ms                                                | 9.21 ms: 1.07x slower                                               |
| regex_effbot             | 3.63 ms                                                | 3.94 ms: 1.08x slower                                               |
| unpickle                 | 14.4 us                                                | 15.8 us: 1.10x slower                                               |
| pickle                   | 10.7 us                                                | 11.8 us: 1.10x slower                                               |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.12x slower                                               |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                               |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.61 ms: 1.28x slower                                               |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x