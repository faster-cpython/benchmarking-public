# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.414x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                       |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                     |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                      |
| tornado_http   | 136 ms                                                 | 89.9 ms: 1.52x faster                                      |
| Geometric mean | (ref)                                                  | 1.39x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.10x faster                                       |
| async_tree_io           | 1.77 sec                                               | 852 ms: 2.08x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 575 ms: 1.77x faster                                       |
| Geometric mean          | (ref)                                                  | 2.04x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.8 ms: 1.73x faster                                      |
| float          | 117 ms                                                 | 79.2 ms: 1.48x faster                                      |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                      |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                       |
| Geometric mean | (ref)                                                  | 1.14x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                       |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                     |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                      |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                      |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.5 ms: 1.14x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                       |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                      |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                      |
| unpickle_list        | 5.20 us                                                | 5.49 us: 1.06x slower                                      |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                      |
| pickle_dict          | 29.6 us                                                | 33.3 us: 1.12x slower                                      |
| Geometric mean       | (ref)                                                  | 1.15x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                      |
| django_template | 48.2 ms                                                | 34.0 ms: 1.42x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| Geometric mean  | (ref)                                                  | 1.37x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                       |
| generators               | 80.1 ms                                                | 27.0 ms: 2.97x faster                                      |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                      |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.10x faster                                       |
| async_tree_io            | 1.77 sec                                               | 852 ms: 2.08x faster                                       |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                       |
| raytrace                 | 507 ms                                                 | 262 ms: 1.94x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.93x faster                                      |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.90x faster                                       |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                       |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                       |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.79x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 72.1 ms: 1.77x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 575 ms: 1.77x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                      |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.75x faster                                       |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                       |
| nbody                    | 154 ms                                                 | 88.8 ms: 1.73x faster                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                      |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                      |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                      |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                       |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                       |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                      |
| tornado_http             | 136 ms                                                 | 89.9 ms: 1.52x faster                                      |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                     |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                       |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                      |
| float                    | 117 ms                                                 | 79.2 ms: 1.48x faster                                      |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                       |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                     |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                      |
| django_template          | 48.2 ms                                                | 34.0 ms: 1.42x faster                                      |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                     |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                     |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                       |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                       |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                       |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                      |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                       |
| dulwich_log              | 84.3 ms                                                | 63.5 ms: 1.33x faster                                      |
| nqueens                  | 106 ms                                                 | 79.9 ms: 1.32x faster                                      |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.31x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                      |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                       |
| scimark_fft              | 466 ms                                                 | 360 ms: 1.29x faster                                       |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                      |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                      |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                       |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                     |
| unpack_sequence          | 60.0 ns                                                | 48.5 ns: 1.24x faster                                      |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                      |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                       |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 87.5 ms: 1.14x faster                                      |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                       |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                       |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                       |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                     |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                      |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                       |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                       |
| pickle_list              | 5.08 us                                                | 5.10 us: 1.00x slower                                      |
| async_generators         | 444 ms                                                 | 447 ms: 1.01x slower                                       |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                      |
| coverage                 | 79.4 ms                                                | 83.6 ms: 1.05x slower                                      |
| unpickle_list            | 5.20 us                                                | 5.49 us: 1.06x slower                                      |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                      |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                      |
| pickle_dict              | 29.6 us                                                | 33.3 us: 1.12x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                      |
| gc_traversal             | 3.62 ms                                                | 4.54 ms: 1.25x slower                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                      |
| bench_mp_pool            | 24.0 ms                                                | 77.9 ms: 3.25x slower                                      |
| Geometric mean           | (ref)                                                  | 1.36x faster                                               |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.414x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x