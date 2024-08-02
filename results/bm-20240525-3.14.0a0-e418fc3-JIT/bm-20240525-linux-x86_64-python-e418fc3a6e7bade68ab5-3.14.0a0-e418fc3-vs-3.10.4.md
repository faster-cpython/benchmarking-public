# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                  |
| chameleon      | 9.68 ms                                                | 7.04 ms: 1.37x faster                                                 |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                |
| html5lib       | 88.9 ms                                                | 68.1 ms: 1.31x faster                                                 |
| tornado_http   | 136 ms                                                 | 97.0 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 385 ms: 1.89x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 466 ms: 1.87x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 957 ms: 1.85x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.8 ms: 1.90x faster                                                 |
| float          | 117 ms                                                 | 72.2 ms: 1.62x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.46x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                 |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                  |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                |
| unpickle_pure_python | 331 us                                                 | 224 us: 1.47x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 81.8 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.34 us: 1.03x slower                                                 |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                 |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.9 us: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                 |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                  |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.72 ms: 2.13x faster                                                 |
| richards_super           | 94.7 ms                                                | 48.0 ms: 1.98x faster                                                 |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 62.1 ms: 1.90x faster                                                 |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                                 |
| nbody                    | 154 ms                                                 | 80.8 ms: 1.90x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                 |
| async_tree_none          | 728 ms                                                 | 385 ms: 1.89x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 466 ms: 1.87x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 957 ms: 1.85x faster                                                  |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 520 ms: 1.77x faster                                                  |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                 |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                  |
| mako                     | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| float                    | 117 ms                                                 | 72.2 ms: 1.62x faster                                                 |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.60x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.56 ms: 1.59x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                 |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                  |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.21 ms: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 38.6 us: 1.51x faster                                                 |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                  |
| fannkuch                 | 532 ms                                                 | 356 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 224 us: 1.47x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                 |
| logging_format           | 9.09 us                                                | 6.29 us: 1.45x faster                                                 |
| scimark_lu               | 176 ms                                                 | 122 ms: 1.44x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| tornado_http             | 136 ms                                                 | 97.0 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                |
| chameleon                | 9.68 ms                                                | 7.04 ms: 1.37x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                 |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                                  |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                 |
| thrift                   | 1.07 ms                                                | 816 us: 1.31x faster                                                  |
| deepcopy                 | 479 us                                                 | 365 us: 1.31x faster                                                  |
| html5lib                 | 88.9 ms                                                | 68.1 ms: 1.31x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.30x faster                                                |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                  |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.35 us: 1.25x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                                 |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 69.3 ms: 1.22x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 81.8 ms: 1.21x faster                                                 |
| dask                     | 441 ms                                                 | 376 ms: 1.17x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                 |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 867 us: 1.14x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| sympy_expand             | 566 ms                                                 | 509 ms: 1.11x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                  |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.34 us: 1.03x slower                                                 |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                 |
| flaskblogging            | 8.58 ms                                                | 9.20 ms: 1.07x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 8.12 ms: 1.12x slower                                                 |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.84 ms: 1.13x slower                                                 |
| coverage                 | 79.4 ms                                                | 94.0 ms: 1.18x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.9 us: 1.21x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                          |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x