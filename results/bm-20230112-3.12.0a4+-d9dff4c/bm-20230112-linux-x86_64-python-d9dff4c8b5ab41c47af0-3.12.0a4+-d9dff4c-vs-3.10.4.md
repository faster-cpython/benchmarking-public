
# Results vs. 3.10.4

- fork: python
- ref: d9dff4c8b5ab41c47af0
- machine: linux-x86_64
- commit hash: d9dff4c
- commit date: 2023-01-12
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.32x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                  |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.4 ms: 1.52x faster                                                  |
| float          | 109 ms                                                 | 72.4 ms: 1.51x faster                                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.61 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.39 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.2 ms: 1.23x faster                                                  |
| json_loads           | 28.7 us                                                | 23.6 us: 1.21x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.04 us: 1.17x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle             | 14.2 us                                                | 12.9 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                                  |
| pickle_dict          | 27.6 us                                                | 30.4 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.58 ms: 1.64x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.13 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                  |
| mako            | 14.7 ms                                                | 9.77 ms: 1.50x faster                                                  |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.27x faster                                                  |
| logging_silent          | 176 ns                                                 | 89.8 ns: 1.96x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                   |
| richards                | 75.2 ms                                                | 41.3 ms: 1.82x faster                                                  |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                                   |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.5 ms: 1.68x faster                                                  |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                   |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                   |
| python_startup          | 14.1 ms                                                | 8.58 ms: 1.64x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                   |
| chaos                   | 106 ms                                                 | 66.8 ms: 1.58x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 74.8 ms: 1.56x faster                                                  |
| spectral_norm           | 150 ms                                                 | 97.1 ms: 1.54x faster                                                  |
| deepcopy_memo           | 51.7 us                                                | 33.8 us: 1.53x faster                                                  |
| nbody                   | 144 ms                                                 | 94.4 ms: 1.52x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                   |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                  |
| float                   | 109 ms                                                 | 72.4 ms: 1.51x faster                                                  |
| mako                    | 14.7 ms                                                | 9.77 ms: 1.50x faster                                                  |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.47x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.39 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                                 |
| pprint_safe_repr        | 953 ms                                                 | 673 ms: 1.42x faster                                                   |
| logging_simple          | 8.10 us                                                | 5.74 us: 1.41x faster                                                  |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                                  |
| logging_format          | 8.85 us                                                | 6.42 us: 1.38x faster                                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                  |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                   |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.11 ms: 1.33x faster                                                  |
| 2to3                    | 335 ms                                                 | 253 ms: 1.32x faster                                                   |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 45.1 ns: 1.32x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 657 ms: 1.30x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.3 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                                   |
| fannkuch                | 488 ms                                                 | 377 ms: 1.29x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                                  |
| coroutines              | 31.6 ms                                                | 24.7 ms: 1.28x faster                                                  |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                                   |
| nqueens                 | 100 ms                                                 | 80.3 ms: 1.25x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.2 ms: 1.23x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 776 us: 1.22x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                                  |
| json_loads              | 28.7 us                                                | 23.6 us: 1.21x faster                                                  |
| async_generators        | 426 ms                                                 | 355 ms: 1.20x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.04 us: 1.17x faster                                                  |
| sympy_expand            | 534 ms                                                 | 458 ms: 1.17x faster                                                   |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                   |
| djangocms               | 36.9 us                                                | 32.1 us: 1.15x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                                  |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.13x faster                                                  |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.50 sec: 1.10x faster                                                 |
| unpickle                | 14.2 us                                                | 12.9 us: 1.09x faster                                                  |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                                   |
| telco                   | 6.73 ms                                                | 6.33 ms: 1.06x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                   |
| generators              | 76.4 ms                                                | 75.4 ms: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.13 ms: 1.06x slower                                                  |
| gc_traversal            | 3.53 ms                                                | 3.80 ms: 1.08x slower                                                  |
| pickle_dict             | 27.6 us                                                | 30.4 us: 1.10x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.61 ms: 1.13x slower                                                  |
| dask                    | 436 ms                                                 | 495 ms: 1.13x slower                                                   |
| coverage                | 74.7 ms                                                | 101 ms: 1.35x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230112-3.12.0a4+-d9dff4c/bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c.json: mypy
