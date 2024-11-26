# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.395x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.32x faster                                       |
| chameleon      | 9.68 ms                                                | 6.96 ms: 1.39x faster                                      |
| docutils       | 3.30 sec                                               | 2.75 sec: 1.20x faster                                     |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.32x faster                                      |
| tornado_http   | 136 ms                                                 | 91.7 ms: 1.49x faster                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 366 ms: 1.99x faster                                       |
| async_tree_io           | 1.77 sec                                               | 902 ms: 1.96x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 455 ms: 1.91x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 595 ms: 1.71x faster                                       |
| Geometric mean          | (ref)                                                  | 1.89x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.6 ms: 1.79x faster                                      |
| float          | 117 ms                                                 | 76.8 ms: 1.52x faster                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.41x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                      |
| regex_dna      | 227 ms                                                 | 232 ms: 1.03x slower                                       |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                       |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 60.9 ms: 1.30x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.3 ms: 1.14x faster                                      |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                       |
| Geometric mean       | (ref)                                                  | 1.28x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                      |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                      |
| genshi_xml      | 66.0 ms                                                | 50.7 ms: 1.30x faster                                      |
| Geometric mean  | (ref)                                                  | 1.39x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                       |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                      |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.44x faster                                      |
| async_tree_none          | 728 ms                                                 | 366 ms: 1.99x faster                                       |
| async_tree_io            | 1.77 sec                                               | 902 ms: 1.96x faster                                       |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                      |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 455 ms: 1.91x faster                                       |
| asyncio_tcp              | 922 ms                                                 | 492 ms: 1.88x faster                                       |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                       |
| nbody                    | 154 ms                                                 | 85.6 ms: 1.79x faster                                      |
| pylint                   | 551 ms                                                 | 309 ms: 1.79x faster                                       |
| richards_super           | 94.7 ms                                                | 54.2 ms: 1.75x faster                                      |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.1 ms: 1.71x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 595 ms: 1.71x faster                                       |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                      |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.67x faster                                       |
| richards                 | 79.3 ms                                                | 48.0 ms: 1.65x faster                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                      |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                       |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                       |
| float                    | 117 ms                                                 | 76.8 ms: 1.52x faster                                      |
| deepcopy_memo            | 58.5 us                                                | 38.5 us: 1.52x faster                                      |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                       |
| pyflate                  | 716 ms                                                 | 481 ms: 1.49x faster                                       |
| tornado_http             | 136 ms                                                 | 91.7 ms: 1.49x faster                                      |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                      |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                       |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                     |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                      |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                     |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                       |
| chameleon                | 9.68 ms                                                | 6.96 ms: 1.39x faster                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                      |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| deepcopy                 | 479 us                                                 | 357 us: 1.34x faster                                       |
| thrift                   | 1.07 ms                                                | 799 us: 1.34x faster                                       |
| nqueens                  | 106 ms                                                 | 78.9 ms: 1.34x faster                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                     |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                       |
| dulwich_log              | 84.3 ms                                                | 63.7 ms: 1.32x faster                                      |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.32x faster                                      |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                       |
| 2to3                     | 348 ms                                                 | 265 ms: 1.32x faster                                       |
| genshi_xml               | 66.0 ms                                                | 50.7 ms: 1.30x faster                                      |
| xml_etree_process        | 79.1 ms                                                | 60.9 ms: 1.30x faster                                      |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.21 us: 1.30x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                      |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                       |
| scimark_fft              | 466 ms                                                 | 370 ms: 1.26x faster                                       |
| mypy2                    | 894 ms                                                 | 717 ms: 1.25x faster                                       |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                       |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                       |
| bench_thread_pool        | 986 us                                                 | 814 us: 1.21x faster                                       |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                      |
| docutils                 | 3.30 sec                                               | 2.75 sec: 1.20x faster                                     |
| xml_etree_generate       | 99.4 ms                                                | 87.3 ms: 1.14x faster                                      |
| json                     | 5.69 ms                                                | 5.01 ms: 1.14x faster                                      |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                       |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                       |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                     |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                       |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                       |
| regex_dna                | 227 ms                                                 | 232 ms: 1.03x slower                                       |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                      |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                      |
| telco                    | 7.27 ms                                                | 8.34 ms: 1.15x slower                                      |
| coverage                 | 79.4 ms                                                | 91.7 ms: 1.15x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                      |
| Geometric mean           | (ref)                                                  | 1.39x faster                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.395x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.13x