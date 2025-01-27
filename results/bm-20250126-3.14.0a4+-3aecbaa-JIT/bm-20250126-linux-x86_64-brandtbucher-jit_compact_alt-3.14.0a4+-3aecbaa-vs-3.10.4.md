# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_compact_alt
- machine: linux-x86_64
- commit hash: 3aecbaa
- commit date: 2025-01-26
- overall geometric mean: 1.392x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.45x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.32x faster                                                    |
| docutils       | 3.30 sec                                               | 2.83 sec: 1.16x faster                                                  |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 637 ms: 2.78x faster                                                    |
| async_tree_none         | 728 ms                                                 | 268 ms: 2.72x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 338 ms: 2.58x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 505 ms: 2.01x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.50x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.6 ms: 1.73x faster                                                   |
| nbody          | 154 ms                                                 | 92.9 ms: 1.65x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.43x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                   |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 332 us: 1.46x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 237 us: 1.40x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 95.7 ms: 1.21x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                   |
| json_loads           | 31.2 us                                                | 29.2 us: 1.07x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.33 ms: 1.24x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.57x faster                                                   |
| django_template | 48.2 ms                                                | 34.7 ms: 1.39x faster                                                   |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 637 ms: 2.78x faster                                                    |
| async_tree_none          | 728 ms                                                 | 268 ms: 2.72x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 338 ms: 2.58x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.38 ms: 2.34x faster                                                   |
| generators               | 80.1 ms                                                | 38.5 ms: 2.08x faster                                                   |
| richards_super           | 94.7 ms                                                | 46.9 ms: 2.02x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 505 ms: 2.01x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                   |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                   |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 69.0 ms: 1.85x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                                   |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                    |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                    |
| raytrace                 | 507 ms                                                 | 290 ms: 1.75x faster                                                    |
| float                    | 117 ms                                                 | 67.6 ms: 1.73x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                   |
| spectral_norm            | 170 ms                                                 | 99.0 ms: 1.72x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.06 ms: 1.72x faster                                                   |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                  |
| nbody                    | 154 ms                                                 | 92.9 ms: 1.65x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                   |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                    |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.57x faster                                                   |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                   |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                    |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 332 us: 1.46x faster                                                    |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                   |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 237 us: 1.40x faster                                                    |
| django_template          | 48.2 ms                                                | 34.7 ms: 1.39x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.72 ms: 1.37x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                   |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 750 ms: 1.36x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.7 ms: 1.32x faster                                                   |
| 2to3                     | 348 ms                                                 | 263 ms: 1.32x faster                                                    |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                    |
| nqueens                  | 106 ms                                                 | 81.2 ms: 1.30x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                    |
| thrift                   | 1.07 ms                                                | 824 us: 1.30x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 56.8 ms: 1.22x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 95.7 ms: 1.21x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                   |
| sympy_str                | 346 ms                                                 | 292 ms: 1.18x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.83 sec: 1.16x faster                                                  |
| sympy_expand             | 566 ms                                                 | 489 ms: 1.16x faster                                                    |
| logging_format           | 9.09 us                                                | 7.87 us: 1.15x faster                                                   |
| logging_simple           | 8.30 us                                                | 7.26 us: 1.14x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                    |
| async_generators         | 444 ms                                                 | 396 ms: 1.12x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 75.6 ms: 1.11x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                   |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                   |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 21.6 ms: 1.08x faster                                                   |
| json_loads               | 31.2 us                                                | 29.2 us: 1.07x faster                                                   |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 166 ms: 1.04x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 972 us: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                    |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.33 ms: 1.24x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.61 ms: 1.27x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 90.2 ms: 3.76x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                            |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250126-3.14.0a4+-3aecbaa-JIT/bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.392x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.45x