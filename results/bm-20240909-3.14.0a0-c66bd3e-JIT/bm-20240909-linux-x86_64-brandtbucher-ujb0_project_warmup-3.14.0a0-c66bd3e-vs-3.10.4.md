# Results vs. 3.10.4

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: c66bd3e
- commit date: 2024-09-09
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 292 ms: 1.19x faster                                                       |
| docutils       | 3.30 sec                                               | 3.46 sec: 1.05x slower                                                     |
| html5lib       | 88.9 ms                                                | 73.0 ms: 1.22x faster                                                      |
| tornado_http   | 136 ms                                                 | 119 ms: 1.15x faster                                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 338 ms: 2.15x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 426 ms: 2.04x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 951 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 573 ms: 1.77x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.95x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.1 ms: 1.85x faster                                                      |
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.47x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                       |
| regex_dna      | 227 ms                                                 | 206 ms: 1.10x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 53.9 ms: 1.47x faster                                                      |
| json_dumps           | 14.2 ms                                                | 9.69 ms: 1.46x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                       |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                                      |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                                      |
| pickle_list          | 5.08 us                                                | 5.21 us: 1.03x slower                                                      |
| unpickle_list        | 5.20 us                                                | 5.39 us: 1.04x slower                                                      |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                      |
| pickle_dict          | 29.6 us                                                | 34.3 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.78 ms: 1.67x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                      |
| django_template | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.41x faster                                                       |
| generators               | 80.1 ms                                                | 34.3 ms: 2.33x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.57 ms: 2.22x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                                      |
| async_tree_none          | 728 ms                                                 | 338 ms: 2.15x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 426 ms: 2.04x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 58.4 ms: 2.02x faster                                                      |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 65.4 ms: 1.95x faster                                                      |
| richards                 | 79.3 ms                                                | 40.9 ms: 1.94x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 951 ms: 1.86x faster                                                       |
| nbody                    | 154 ms                                                 | 83.1 ms: 1.85x faster                                                      |
| richards_super           | 94.7 ms                                                | 51.4 ms: 1.84x faster                                                      |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 573 ms: 1.77x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 520 ms: 1.77x faster                                                       |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                       |
| raytrace                 | 507 ms                                                 | 289 ms: 1.75x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                      |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                       |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                      |
| mako                     | 16.3 ms                                                | 9.78 ms: 1.67x faster                                                      |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                                       |
| pyflate                  | 716 ms                                                 | 441 ms: 1.62x faster                                                       |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.20 ms: 1.54x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                     |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.51x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 53.9 ms: 1.47x faster                                                      |
| json_dumps               | 14.2 ms                                                | 9.69 ms: 1.46x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.27 ms: 1.43x faster                                                      |
| fannkuch                 | 532 ms                                                 | 374 ms: 1.42x faster                                                       |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.88 us: 1.41x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                     |
| thrift                   | 1.07 ms                                                | 795 us: 1.35x faster                                                       |
| logging_format           | 9.09 us                                                | 6.74 us: 1.35x faster                                                      |
| go                       | 240 ms                                                 | 178 ms: 1.35x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.30x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.69 ms: 1.28x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                      |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                                      |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                       |
| html5lib                 | 88.9 ms                                                | 73.0 ms: 1.22x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 2.15 ms: 1.20x faster                                                      |
| 2to3                     | 348 ms                                                 | 292 ms: 1.19x faster                                                       |
| django_template          | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.34 sec: 1.17x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                       |
| tornado_http             | 136 ms                                                 | 119 ms: 1.15x faster                                                       |
| pylint                   | 551 ms                                                 | 482 ms: 1.14x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 126 ms: 1.14x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 895 us: 1.10x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                      |
| regex_dna                | 227 ms                                                 | 206 ms: 1.10x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                                      |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                      |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 67.8 ms: 1.02x faster                                                      |
| sympy_expand             | 566 ms                                                 | 557 ms: 1.02x faster                                                       |
| sympy_str                | 346 ms                                                 | 341 ms: 1.01x faster                                                       |
| bench_mp_pool            | 24.0 ms                                                | 24.2 ms: 1.01x slower                                                      |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                                      |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                       |
| pickle_list              | 5.08 us                                                | 5.21 us: 1.03x slower                                                      |
| unpickle_list            | 5.20 us                                                | 5.39 us: 1.04x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                                      |
| docutils                 | 3.30 sec                                               | 3.46 sec: 1.05x slower                                                     |
| sympy_integrate          | 25.8 ms                                                | 27.6 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 85.9 ms: 1.08x slower                                                      |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.09x slower                                                      |
| sympy_sum                | 196 ms                                                 | 215 ms: 1.10x slower                                                       |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.12x slower                                                      |
| pickle_dict              | 29.6 us                                                | 34.3 us: 1.16x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                      |
| unpack_sequence          | 60.0 ns                                                | 138 ns: 2.31x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240909-3.14.0a0-c66bd3e-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.34x