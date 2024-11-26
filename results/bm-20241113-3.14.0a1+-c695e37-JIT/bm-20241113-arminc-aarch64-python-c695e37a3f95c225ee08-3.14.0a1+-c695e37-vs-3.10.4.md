# Results vs. 3.10.4

- fork: python
- ref: c695e37a3f95c225ee08
- machine: linux-aarch64
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.158x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 398 ms: 1.05x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.79 sec: 1.07x slower                                                   |
| html5lib       | 86.5 ms                                                               | 73.7 ms: 1.17x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 477 ms: 1.99x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 618 ms: 1.83x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 790 ms: 1.61x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.84x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 116 ms: 1.44x faster                                                     |
| float          | 135 ms                                                                | 94.6 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.25 ms                                                               | 5.20 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 270 us: 1.35x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 399 us: 1.33x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 82.6 ms: 1.21x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 197 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.04x faster                                                     |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| genshi_text    | 35.2 ms                                                               | 33.6 ms: 1.05x faster                                                    |
| genshi_xml     | 69.8 ms                                                               | 84.6 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 225 us: 2.93x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.30 ms: 2.08x faster                                                    |
| async_tree_none          | 950 ms                                                                | 477 ms: 1.99x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 618 ms: 1.83x faster                                                     |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 790 ms: 1.61x faster                                                     |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                     |
| raytrace                 | 573 ms                                                                | 368 ms: 1.56x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 40.8 us: 1.51x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 90.8 ms: 1.48x faster                                                    |
| richards_super           | 107 ms                                                                | 73.8 ms: 1.45x faster                                                    |
| scimark_lu               | 227 ms                                                                | 158 ms: 1.44x faster                                                     |
| nbody                    | 166 ms                                                                | 116 ms: 1.44x faster                                                     |
| go                       | 264 ms                                                                | 185 ms: 1.43x faster                                                     |
| float                    | 135 ms                                                                | 94.6 ms: 1.42x faster                                                    |
| richards                 | 91.7 ms                                                               | 64.4 ms: 1.42x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.71 ms: 1.41x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 91.6 ms: 1.40x faster                                                    |
| chaos                    | 121 ms                                                                | 87.3 ms: 1.39x faster                                                    |
| generators               | 68.1 ms                                                               | 49.3 ms: 1.38x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 270 us: 1.35x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 399 us: 1.33x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.14 ms: 1.33x faster                                                    |
| comprehensions           | 33.1 us                                                               | 25.2 us: 1.31x faster                                                    |
| pyflate                  | 795 ms                                                                | 609 ms: 1.30x faster                                                     |
| deepcopy                 | 511 us                                                                | 399 us: 1.28x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.73 us: 1.27x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.42 us: 1.26x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                    |
| spectral_norm            | 186 ms                                                                | 150 ms: 1.24x faster                                                     |
| thrift                   | 1.26 ms                                                               | 1.02 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 82.6 ms: 1.21x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 73.7 ms: 1.17x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.41 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 455 ms: 1.10x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.18 us: 1.10x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.55 sec: 1.09x faster                                                   |
| fannkuch                 | 546 ms                                                                | 502 ms: 1.09x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 10.1 ms: 1.08x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 197 ms: 1.08x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 33.6 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.04x faster                                                     |
| json                     | 5.88 ms                                                               | 5.74 ms: 1.02x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.65 sec: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 683 ms: 1.04x slower                                                     |
| nqueens                  | 117 ms                                                                | 123 ms: 1.04x slower                                                     |
| 2to3                     | 381 ms                                                                | 398 ms: 1.05x slower                                                     |
| sqlglot_normalize        | 156 ms                                                                | 164 ms: 1.05x slower                                                     |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.79 sec: 1.07x slower                                                   |
| sympy_str                | 329 ms                                                                | 356 ms: 1.08x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.26 sec: 1.10x slower                                                   |
| sympy_expand             | 543 ms                                                                | 596 ms: 1.10x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 80.9 ms: 1.10x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.4 ms: 1.11x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 84.7 ms: 1.12x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.66 sec: 1.13x slower                                                   |
| sympy_sum                | 184 ms                                                                | 212 ms: 1.15x slower                                                     |
| async_generators         | 452 ms                                                                | 529 ms: 1.17x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.98 ms: 1.18x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 84.6 ms: 1.21x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 5.20 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.43 ms: 1.55x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.83 ms: 1.69x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.37 sec: 163.21x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (11): scimark_sparse_mat_mult, sqlalchemy_imperative, sqlalchemy_declarative, meteor_contest, django_template, sqlite_synth, regex_dna, regex_compile, pidigits, pylint, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.158x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.38x