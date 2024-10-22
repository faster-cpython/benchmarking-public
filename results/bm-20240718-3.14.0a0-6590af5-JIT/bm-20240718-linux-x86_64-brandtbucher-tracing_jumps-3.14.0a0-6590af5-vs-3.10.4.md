# Results vs. 3.10.4

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 6590af5
- commit date: 2024-07-18
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                 |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.15x faster                                               |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                |
| tornado_http   | 136 ms                                                 | 92.5 ms: 1.47x faster                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 330 ms: 2.21x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 413 ms: 2.11x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 861 ms: 2.05x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.4 ms: 1.86x faster                                                |
| float          | 117 ms                                                 | 71.8 ms: 1.63x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.46x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                 |
| regex_effbot   | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.65x faster                                               |
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                 |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                                |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.65 ms: 1.69x faster                                                |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                |
| genshi_xml      | 66.0 ms                                                | 53.5 ms: 1.23x faster                                                |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                 |
| generators               | 80.1 ms                                                | 33.0 ms: 2.43x faster                                                |
| deltablue                | 7.91 ms                                                | 3.57 ms: 2.22x faster                                                |
| async_tree_none          | 728 ms                                                 | 330 ms: 2.21x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 413 ms: 2.11x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 861 ms: 2.05x faster                                                 |
| richards_super           | 94.7 ms                                                | 46.5 ms: 2.04x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 60.4 ms: 1.96x faster                                                |
| richards                 | 79.3 ms                                                | 40.8 ms: 1.94x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                |
| raytrace                 | 507 ms                                                 | 269 ms: 1.89x faster                                                 |
| nbody                    | 154 ms                                                 | 82.4 ms: 1.86x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                                 |
| logging_silent           | 190 ns                                                 | 106 ns: 1.78x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                |
| deepcopy                 | 479 us                                                 | 276 us: 1.74x faster                                                 |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.71x faster                                                 |
| pyflate                  | 716 ms                                                 | 421 ms: 1.70x faster                                                 |
| mako                     | 16.3 ms                                                | 9.65 ms: 1.69x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.65x faster                                               |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                 |
| float                    | 117 ms                                                 | 71.8 ms: 1.63x faster                                                |
| pylint                   | 551 ms                                                 | 339 ms: 1.62x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                                |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                                |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.35 ms: 1.49x faster                                                |
| fannkuch                 | 532 ms                                                 | 358 ms: 1.49x faster                                                 |
| tornado_http             | 136 ms                                                 | 92.5 ms: 1.47x faster                                                |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                               |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                 |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                               |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                |
| thrift                   | 1.07 ms                                                | 803 us: 1.33x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                 |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                 |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 55.3 ms: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                                |
| genshi_xml               | 66.0 ms                                                | 53.5 ms: 1.23x faster                                                |
| dask                     | 441 ms                                                 | 363 ms: 1.22x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 826 us: 1.19x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                |
| sympy_str                | 346 ms                                                 | 297 ms: 1.16x faster                                                 |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                 |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.15x faster                                               |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                                |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                               |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                 |
| async_generators         | 444 ms                                                 | 451 ms: 1.02x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.71 ms: 1.02x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                |
| telco                    | 7.27 ms                                                | 8.08 ms: 1.11x slower                                                |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240718-3.14.0a0-6590af5-JIT/bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x