# Results vs. 3.10.4

- fork: faster-cpython
- ref: load_fast_can_be_def
- machine: linux-x86_64
- commit hash: cb9433d
- commit date: 2024-10-04
- overall geometric mean: 1.425x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.35x faster                                                            |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                           |
| tornado_http   | 136 ms                                                 | 91.7 ms: 1.49x faster                                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 312 ms: 2.33x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 392 ms: 2.22x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 874 ms: 2.02x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.09x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.0 ms: 1.74x faster                                                           |
| float          | 117 ms                                                 | 77.1 ms: 1.52x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                           |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                           |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                            |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.32 us: 1.02x slower                                                           |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                           |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                            |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                           |
| async_tree_none          | 728 ms                                                 | 312 ms: 2.33x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 392 ms: 2.22x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 874 ms: 2.02x faster                                                            |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 469 ms: 1.96x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                           |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                            |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                                           |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                            |
| richards_super           | 94.7 ms                                                | 53.2 ms: 1.78x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 72.3 ms: 1.77x faster                                                           |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.74x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                           |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                            |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                           |
| richards                 | 79.3 ms                                                | 46.9 ms: 1.69x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.57x faster                                                           |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                            |
| float                    | 117 ms                                                 | 77.1 ms: 1.52x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                           |
| pyflate                  | 716 ms                                                 | 477 ms: 1.50x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| tornado_http             | 136 ms                                                 | 91.7 ms: 1.49x faster                                                           |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.77 sec: 1.45x faster                                                          |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                            |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.43x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                            |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                           |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                          |
| 2to3                     | 348 ms                                                 | 257 ms: 1.35x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                            |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                            |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                           |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 65.5 ms: 1.29x faster                                                           |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.08 ms: 1.27x faster                                                           |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.26x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                          |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                            |
| unpack_sequence          | 60.0 ns                                                | 50.9 ns: 1.18x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 850 us: 1.16x faster                                                            |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                          |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                            |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                           |
| async_generators         | 444 ms                                                 | 433 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.32 us: 1.02x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.06x slower                                                           |
| coverage                 | 79.4 ms                                                | 85.6 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 8.00 ms: 1.10x slower                                                           |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.1 ms: 2.34x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241004-3.14.0a0-cb9433d/bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.425x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x