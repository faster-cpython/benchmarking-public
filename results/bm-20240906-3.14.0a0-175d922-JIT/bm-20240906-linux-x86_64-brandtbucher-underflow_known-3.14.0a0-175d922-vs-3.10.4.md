# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 175d922
- commit date: 2024-09-06
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                   |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.09x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                  |
| tornado_http   | 136 ms                                                 | 97.0 ms: 1.41x faster                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 938 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.5 ms: 1.93x faster                                                  |
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.49x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.32x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                  |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                   |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                  |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                                  |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                  |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                  |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                  |
| generators               | 80.1 ms                                                | 33.3 ms: 2.41x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 26.0 us: 2.25x faster                                                  |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                   |
| richards_super           | 94.7 ms                                                | 42.6 ms: 2.22x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                                   |
| logging_silent           | 190 ns                                                 | 94.5 ns: 2.01x faster                                                  |
| richards                 | 79.3 ms                                                | 40.0 ms: 1.98x faster                                                  |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                  |
| nbody                    | 154 ms                                                 | 79.5 ms: 1.93x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                                  |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 938 ms: 1.89x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 495 ms: 1.86x faster                                                   |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                   |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                   |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                  |
| spectral_norm            | 170 ms                                                 | 99.7 ms: 1.70x faster                                                  |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                                  |
| mako                     | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                 |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                   |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.37 ms: 1.58x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.23 ms: 1.53x faster                                                  |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.53x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.88 ms: 1.51x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.50x faster                                                  |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                 |
| fannkuch                 | 532 ms                                                 | 376 ms: 1.41x faster                                                   |
| tornado_http             | 136 ms                                                 | 97.0 ms: 1.41x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                  |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                  |
| regex_compile            | 188 ms                                                 | 142 ms: 1.32x faster                                                   |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                   |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                   |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 842 us: 1.17x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                  |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                   |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                   |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                                  |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                  |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.66 ms: 1.01x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.18 us: 1.02x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                  |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                                  |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                  |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                  |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                  |
| unpack_sequence          | 60.0 ns                                                | 111 ns: 1.85x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                           |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240906-3.14.0a0-175d922-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.22x