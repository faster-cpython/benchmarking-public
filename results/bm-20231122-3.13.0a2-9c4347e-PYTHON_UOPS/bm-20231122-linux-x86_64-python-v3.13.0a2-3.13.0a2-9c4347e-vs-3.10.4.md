
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 288 ms: 1.21x faster                                       |
| chameleon      | 9.68 ms                                                | 7.54 ms: 1.29x faster                                      |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                     |
| tornado_http   | 136 ms                                                 | 99.5 ms: 1.37x faster                                      |
| Geometric mean | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 456 ms: 1.60x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 583 ms: 1.49x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.45x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 731 ms: 1.39x faster                                       |
| Geometric mean          | (ref)                                                  | 1.48x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 119 ms: 1.30x faster                                       |
| float          | 117 ms                                                 | 92.4 ms: 1.27x faster                                      |
| pidigits       | 191 ms                                                 | 196 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.17x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 157 ms: 1.20x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                      |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                       |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                       |
| unpickle_pure_python | 331 us                                                 | 240 us: 1.38x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                      |
| tomli_loads          | 3.14 sec                                               | 2.39 sec: 1.31x faster                                     |
| xml_etree_process    | 79.1 ms                                                | 61.8 ms: 1.28x faster                                      |
| json_loads           | 31.2 us                                                | 28.2 us: 1.10x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 90.2 ms: 1.10x faster                                      |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                       |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.04x faster                                       |
| pickle_list          | 5.08 us                                                | 4.94 us: 1.03x faster                                      |
| pickle               | 10.7 us                                                | 11.1 us: 1.04x slower                                      |
| unpickle             | 14.4 us                                                | 15.6 us: 1.08x slower                                      |
| pickle_dict          | 29.6 us                                                | 34.0 us: 1.15x slower                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.3 ms: 1.41x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 9.00 ms: 1.52x slower                                      |
| Geometric mean         | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 16.3 ms                                                | 13.7 ms: 1.19x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 122 us: 4.45x faster                                       |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                       |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                       |
| deltablue                | 7.91 ms                                                | 4.67 ms: 1.69x faster                                      |
| richards_super           | 94.7 ms                                                | 57.2 ms: 1.66x faster                                      |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                       |
| raytrace                 | 507 ms                                                 | 310 ms: 1.63x faster                                       |
| async_tree_none          | 728 ms                                                 | 456 ms: 1.60x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.59x faster                                      |
| richards                 | 79.3 ms                                                | 49.8 ms: 1.59x faster                                      |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                       |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.56x faster                                      |
| chaos                    | 115 ms                                                 | 74.2 ms: 1.56x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 83.3 ms: 1.53x faster                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 583 ms: 1.49x faster                                       |
| go                       | 240 ms                                                 | 163 ms: 1.47x faster                                       |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 81.4 ms: 1.45x faster                                      |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                     |
| deepcopy_memo            | 58.5 us                                                | 41.0 us: 1.43x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                     |
| python_startup           | 14.6 ms                                                | 10.3 ms: 1.41x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 731 ms: 1.39x faster                                       |
| comprehensions           | 28.8 us                                                | 20.9 us: 1.38x faster                                      |
| logging_simple           | 8.30 us                                                | 6.03 us: 1.38x faster                                      |
| pyflate                  | 716 ms                                                 | 521 ms: 1.38x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 240 us: 1.38x faster                                       |
| tornado_http             | 136 ms                                                 | 99.5 ms: 1.37x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                      |
| unpack_sequence          | 60.0 ns                                                | 44.8 ns: 1.34x faster                                      |
| deepcopy                 | 479 us                                                 | 362 us: 1.33x faster                                       |
| logging_format           | 9.09 us                                                | 6.86 us: 1.32x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.18 us: 1.31x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.39 sec: 1.31x faster                                     |
| nbody                    | 154 ms                                                 | 119 ms: 1.30x faster                                       |
| chameleon                | 9.68 ms                                                | 7.54 ms: 1.29x faster                                      |
| xml_etree_process        | 79.1 ms                                                | 61.8 ms: 1.28x faster                                      |
| float                    | 117 ms                                                 | 92.4 ms: 1.27x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 809 ms: 1.26x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.68 sec: 1.26x faster                                     |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                     |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                       |
| sympy_sum                | 196 ms                                                 | 160 ms: 1.23x faster                                       |
| hexiom                   | 10.4 ms                                                | 8.49 ms: 1.22x faster                                      |
| dulwich_log              | 84.3 ms                                                | 69.0 ms: 1.22x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 21.3 ms: 1.21x faster                                      |
| 2to3                     | 348 ms                                                 | 288 ms: 1.21x faster                                       |
| spectral_norm            | 170 ms                                                 | 140 ms: 1.21x faster                                       |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                     |
| regex_compile            | 188 ms                                                 | 157 ms: 1.20x faster                                       |
| mako                     | 16.3 ms                                                | 13.7 ms: 1.19x faster                                      |
| dask                     | 441 ms                                                 | 372 ms: 1.19x faster                                       |
| fannkuch                 | 532 ms                                                 | 450 ms: 1.18x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 58.5 ms: 1.18x faster                                      |
| sympy_str                | 346 ms                                                 | 294 ms: 1.17x faster                                       |
| bench_thread_pool        | 986 us                                                 | 854 us: 1.16x faster                                       |
| sympy_expand             | 566 ms                                                 | 493 ms: 1.15x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.74 ms: 1.13x faster                                      |
| nqueens                  | 106 ms                                                 | 94.1 ms: 1.12x faster                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.46 ms: 1.11x faster                                      |
| json_loads               | 31.2 us                                                | 28.2 us: 1.10x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 90.2 ms: 1.10x faster                                      |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                      |
| pathlib                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                      |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                      |
| scimark_fft              | 466 ms                                                 | 436 ms: 1.07x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                       |
| sqlite_synth             | 3.02 us                                                | 2.91 us: 1.04x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.04x faster                                       |
| meteor_contest           | 120 ms                                                 | 116 ms: 1.03x faster                                       |
| pickle_list              | 5.08 us                                                | 4.94 us: 1.03x faster                                      |
| mdp                      | 2.85 sec                                               | 2.79 sec: 1.02x faster                                     |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                       |
| pidigits                 | 191 ms                                                 | 196 ms: 1.03x slower                                       |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                      |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                       |
| pickle                   | 10.7 us                                                | 11.1 us: 1.04x slower                                      |
| unpickle                 | 14.4 us                                                | 15.6 us: 1.08x slower                                      |
| pickle_dict              | 29.6 us                                                | 34.0 us: 1.15x slower                                      |
| telco                    | 7.27 ms                                                | 8.46 ms: 1.16x slower                                      |
| gc_traversal             | 3.62 ms                                                | 4.29 ms: 1.18x slower                                      |
| coverage                 | 79.4 ms                                                | 95.6 ms: 1.20x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 9.00 ms: 1.52x slower                                      |
| Geometric mean           | (ref)                                                  | 1.26x faster                                               |

Benchmark hidden because not significant (3): mypy2, bench_mp_pool, unpickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x


# Memory

- memory change: 1.05x