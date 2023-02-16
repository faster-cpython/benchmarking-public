
# Results vs. 3.11.0

- fork: DinoV
- ref: coro_freelist
- machine: linux-x86_64
- commit hash: a371554
- commit date: 2023-01-19
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                           |
| chameleon      | 6.38 ms                                                | 6.31 ms: 1.01x faster                                          |
| docutils       | 2.60 sec                                               | 2.47 sec: 1.05x faster                                         |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.09x faster                                          |
| tornado_http   | 96.5 ms                                                | 93.7 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.7 ms: 1.07x faster                                          |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                           |
| nbody          | 90.0 ms                                                | 94.2 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                           |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                          |
| regex_effbot   | 3.46 ms                                                | 3.36 ms: 1.03x faster                                          |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.39 ms: 1.32x faster                                          |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                           |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                           |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                           |
| json_loads           | 26.1 us                                                | 24.0 us: 1.08x faster                                          |
| pickle_dict          | 31.2 us                                                | 29.7 us: 1.05x faster                                          |
| pickle_list          | 4.14 us                                                | 4.03 us: 1.03x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                           |
| xml_etree_generate   | 75.9 ms                                                | 77.1 ms: 1.02x slower                                          |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                   |

Benchmark hidden because not significant (3): unpickle, unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.86 ms: 1.03x slower                                          |
| python_startup_no_site | 6.04 ms                                                | 6.42 ms: 1.06x slower                                          |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.3 ms: 1.09x faster                                          |
| mako           | 9.83 ms                                                | 9.59 ms: 1.03x faster                                          |
| genshi_text    | 21.5 ms                                                | 21.4 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 501 ms: 1.76x faster                                           |
| json_dumps              | 12.4 ms                                                | 9.39 ms: 1.32x faster                                          |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                           |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                          |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.06 ms: 1.13x faster                                          |
| coroutines              | 26.2 ms                                                | 23.2 ms: 1.13x faster                                          |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.10x faster                                         |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                           |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                          |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                           |
| genshi_xml              | 51.4 ms                                                | 47.3 ms: 1.09x faster                                          |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.09x faster                                          |
| nqueens                 | 83.8 ms                                                | 77.1 ms: 1.09x faster                                          |
| json_loads              | 26.1 us                                                | 24.0 us: 1.08x faster                                          |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                           |
| deepcopy_memo           | 35.8 us                                                | 33.4 us: 1.07x faster                                          |
| unpack_sequence         | 44.5 ns                                                | 41.5 ns: 1.07x faster                                          |
| float                   | 76.8 ms                                                | 71.7 ms: 1.07x faster                                          |
| logging_silent          | 98.0 ns                                                | 91.6 ns: 1.07x faster                                          |
| pprint_pformat          | 1.46 sec                                               | 1.36 sec: 1.07x faster                                         |
| pprint_safe_repr        | 706 ms                                                 | 663 ms: 1.06x faster                                           |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                           |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                           |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                          |
| coverage                | 99.3 ms                                                | 93.9 ms: 1.06x faster                                          |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.06x faster                                           |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                          |
| hexiom                  | 6.34 ms                                                | 6.03 ms: 1.05x faster                                          |
| docutils                | 2.60 sec                                               | 2.47 sec: 1.05x faster                                         |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                          |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                           |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                          |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                          |
| pickle_dict             | 31.2 us                                                | 29.7 us: 1.05x faster                                          |
| spectral_norm           | 98.1 ms                                                | 93.8 ms: 1.05x faster                                          |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                           |
| mdp                     | 2.63 sec                                               | 2.52 sec: 1.04x faster                                         |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                          |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                           |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                           |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                           |
| sympy_str               | 291 ms                                                 | 280 ms: 1.04x faster                                           |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                           |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                           |
| scimark_fft             | 325 ms                                                 | 314 ms: 1.04x faster                                           |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                          |
| scimark_monte_carlo     | 68.0 ms                                                | 65.8 ms: 1.03x faster                                          |
| dulwich_log             | 64.0 ms                                                | 62.0 ms: 1.03x faster                                          |
| tornado_http            | 96.5 ms                                                | 93.7 ms: 1.03x faster                                          |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                           |
| regex_effbot            | 3.46 ms                                                | 3.36 ms: 1.03x faster                                          |
| pickle_list             | 4.14 us                                                | 4.03 us: 1.03x faster                                          |
| mako                    | 9.83 ms                                                | 9.59 ms: 1.03x faster                                          |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                          |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                          |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                           |
| crypto_pyaes            | 75.7 ms                                                | 74.5 ms: 1.02x faster                                          |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                           |
| telco                   | 6.43 ms                                                | 6.33 ms: 1.02x faster                                          |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                           |
| chaos                   | 68.7 ms                                                | 67.9 ms: 1.01x faster                                          |
| thrift                  | 760 us                                                 | 751 us: 1.01x faster                                           |
| chameleon               | 6.38 ms                                                | 6.31 ms: 1.01x faster                                          |
| genshi_text             | 21.5 ms                                                | 21.4 ms: 1.01x faster                                          |
| async_generators        | 356 ms                                                 | 357 ms: 1.00x slower                                           |
| async_tree_cpu_io_mixed | 736 ms                                                 | 746 ms: 1.01x slower                                           |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                         |
| xml_etree_generate      | 75.9 ms                                                | 77.1 ms: 1.02x slower                                          |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.02x slower                                           |
| sqlglot_transpile       | 1.65 ms                                                | 1.68 ms: 1.02x slower                                          |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                          |
| sqlglot_parse           | 1.36 ms                                                | 1.39 ms: 1.02x slower                                          |
| python_startup          | 8.58 ms                                                | 8.86 ms: 1.03x slower                                          |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                          |
| async_tree_memoization  | 624 ms                                                 | 646 ms: 1.04x slower                                           |
| generators              | 73.5 ms                                                | 76.7 ms: 1.04x slower                                          |
| nbody                   | 90.0 ms                                                | 94.2 ms: 1.05x slower                                          |
| python_startup_no_site  | 6.04 ms                                                | 6.42 ms: 1.06x slower                                          |
| gc_traversal            | 3.82 ms                                                | 4.29 ms: 1.12x slower                                          |
| dask                    | 365 ms                                                 | 495 ms: 1.36x slower                                           |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (10): unpickle, unpickle_list, scimark_lu, xml_etree_process, go, djangocms, pathlib, bench_mp_pool, async_tree_none, django_template
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230119-3.12.0a4+-a371554/bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554.json: mypy
