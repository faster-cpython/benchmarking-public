# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.393x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                       |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                     |
| html5lib       | 88.9 ms                                                | 63.7 ms: 1.40x faster                                      |
| tornado_http   | 136 ms                                                 | 94.3 ms: 1.45x faster                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 416 ms: 2.09x faster                                       |
| async_tree_io           | 1.77 sec                                               | 856 ms: 2.07x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 576 ms: 1.76x faster                                       |
| Geometric mean          | (ref)                                                  | 2.02x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.3 ms: 1.89x faster                                      |
| float          | 117 ms                                                 | 75.4 ms: 1.55x faster                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.44x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.34x faster                                       |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                      |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                     |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                       |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                       |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                      |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 78.6 ms: 1.26x faster                                      |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 99.9 ms: 1.16x faster                                      |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                       |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                      |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                      |
| unpickle_list        | 5.20 us                                                | 5.59 us: 1.08x slower                                      |
| pickle               | 10.7 us                                                | 12.0 us: 1.12x slower                                      |
| pickle_dict          | 29.6 us                                                | 35.8 us: 1.21x slower                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.22x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                      |
| django_template | 48.2 ms                                                | 37.2 ms: 1.29x faster                                      |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.27x faster                                      |
| genshi_xml      | 66.0 ms                                                | 58.9 ms: 1.12x faster                                      |
| Geometric mean  | (ref)                                                  | 1.31x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                       |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                      |
| generators               | 80.1 ms                                                | 35.4 ms: 2.26x faster                                      |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 416 ms: 2.09x faster                                       |
| async_tree_io            | 1.77 sec                                               | 856 ms: 2.07x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                      |
| richards_super           | 94.7 ms                                                | 48.0 ms: 1.97x faster                                      |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                      |
| logging_silent           | 190 ns                                                 | 98.0 ns: 1.94x faster                                      |
| richards                 | 79.3 ms                                                | 41.0 ms: 1.93x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                      |
| nbody                    | 154 ms                                                 | 81.3 ms: 1.89x faster                                      |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                       |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                       |
| go                       | 240 ms                                                 | 133 ms: 1.81x faster                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 576 ms: 1.76x faster                                       |
| deepcopy                 | 479 us                                                 | 273 us: 1.76x faster                                       |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                      |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                      |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                      |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                       |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                       |
| float                    | 117 ms                                                 | 75.4 ms: 1.55x faster                                      |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                      |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                      |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                       |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                      |
| hexiom                   | 10.4 ms                                                | 7.03 ms: 1.48x faster                                      |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.48x faster                                      |
| pylint                   | 551 ms                                                 | 376 ms: 1.47x faster                                       |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                       |
| tornado_http             | 136 ms                                                 | 94.3 ms: 1.45x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                     |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                     |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                       |
| html5lib                 | 88.9 ms                                                | 63.7 ms: 1.40x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.72 ms: 1.37x faster                                      |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                       |
| regex_compile            | 188 ms                                                 | 140 ms: 1.34x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                      |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                     |
| django_template          | 48.2 ms                                                | 37.2 ms: 1.29x faster                                      |
| dulwich_log              | 84.3 ms                                                | 66.5 ms: 1.27x faster                                      |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.27x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 78.6 ms: 1.26x faster                                      |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                      |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                       |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.22x faster                                      |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                      |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.9 ms: 1.16x faster                                      |
| json                     | 5.69 ms                                                | 4.95 ms: 1.15x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 60.2 ms: 1.15x faster                                      |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                       |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                     |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                       |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.13x faster                                       |
| genshi_xml               | 66.0 ms                                                | 58.9 ms: 1.12x faster                                      |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.12x faster                                       |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 23.6 ms: 1.09x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                      |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                      |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                       |
| pickle_list              | 5.08 us                                                | 5.20 us: 1.02x slower                                      |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                      |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                      |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.07x slower                                      |
| unpickle_list            | 5.20 us                                                | 5.59 us: 1.08x slower                                      |
| async_generators         | 444 ms                                                 | 478 ms: 1.08x slower                                       |
| pickle                   | 10.7 us                                                | 12.0 us: 1.12x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                      |
| pickle_dict              | 29.6 us                                                | 35.8 us: 1.21x slower                                      |
| gc_traversal             | 3.62 ms                                                | 4.40 ms: 1.21x slower                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                      |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.84x slower                                       |
| bench_mp_pool            | 24.0 ms                                                | 84.2 ms: 3.51x slower                                      |
| Geometric mean           | (ref)                                                  | 1.33x faster                                               |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.393x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.33x