# Results vs. 3.10.4

- fork: nohlson
- ref: enable_fcf_protectio
- machine: linux-x86_64
- commit hash: 34aead4
- commit date: 2024-06-25
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.32x faster                                                   |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 67.6 ms: 1.31x faster                                                  |
| tornado_http   | 136 ms                                                 | 90.9 ms: 1.50x faster                                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 363 ms: 2.01x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 920 ms: 1.92x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 481 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 610 ms: 1.66x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.85x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.2 ms: 1.74x faster                                                  |
| float          | 117 ms                                                 | 77.1 ms: 1.52x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                   |
| regex_v8       | 27.8 ms                                                | 26.9 ms: 1.03x faster                                                  |
| regex_dna      | 227 ms                                                 | 232 ms: 1.02x slower                                                   |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                  |
| json_loads           | 31.2 us                                                | 28.5 us: 1.10x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.12 us: 1.01x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.31 us: 1.02x slower                                                  |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                                  |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                  |
| pickle_dict          | 29.6 us                                                | 35.3 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                  |
| django_template | 48.2 ms                                                | 34.7 ms: 1.39x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.3 ms: 1.37x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 51.6 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                                   |
| generators               | 80.1 ms                                                | 29.0 ms: 2.77x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                  |
| async_tree_none          | 728 ms                                                 | 363 ms: 2.01x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                  |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 920 ms: 1.92x faster                                                   |
| raytrace                 | 507 ms                                                 | 265 ms: 1.92x faster                                                   |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                   |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 481 ms: 1.81x faster                                                   |
| pylint                   | 551 ms                                                 | 308 ms: 1.79x faster                                                   |
| richards_super           | 94.7 ms                                                | 53.6 ms: 1.77x faster                                                  |
| nbody                    | 154 ms                                                 | 88.2 ms: 1.74x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.9 ms: 1.72x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.17 ms: 1.68x faster                                                  |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                  |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 610 ms: 1.66x faster                                                   |
| richards                 | 79.3 ms                                                | 47.6 ms: 1.66x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.57x faster                                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                   |
| float                    | 117 ms                                                 | 77.1 ms: 1.52x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                                  |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.52x faster                                                   |
| tornado_http             | 136 ms                                                 | 90.9 ms: 1.50x faster                                                  |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                  |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                 |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                 |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                  |
| django_template          | 48.2 ms                                                | 34.7 ms: 1.39x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.39x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.3 ms: 1.37x faster                                                  |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                   |
| thrift                   | 1.07 ms                                                | 793 us: 1.35x faster                                                   |
| nqueens                  | 106 ms                                                 | 78.8 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                   |
| 2to3                     | 348 ms                                                 | 265 ms: 1.32x faster                                                   |
| html5lib                 | 88.9 ms                                                | 67.6 ms: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.4 ms: 1.31x faster                                                  |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.04 ms: 1.28x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 51.6 ms: 1.28x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 54.1 ms: 1.28x faster                                                  |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                                   |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 791 us: 1.25x faster                                                   |
| dask                     | 441 ms                                                 | 357 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                 |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| json_loads               | 31.2 us                                                | 28.5 us: 1.10x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.04x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.9 ms: 1.03x faster                                                  |
| async_generators         | 444 ms                                                 | 430 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                   |
| pickle_list              | 5.08 us                                                | 5.12 us: 1.01x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.31 us: 1.02x slower                                                  |
| regex_dna                | 227 ms                                                 | 232 ms: 1.02x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                                  |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                  |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                  |
| telco                    | 7.27 ms                                                | 8.24 ms: 1.13x slower                                                  |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                  |
| pickle_dict              | 29.6 us                                                | 35.3 us: 1.19x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240625-3.14.0a0-34aead4/bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.11x