
# Results vs. 3.11.0

- fork: DinoV
- ref: coro_freelist
- machine: linux-x86_64
- commit hash: a371554
- commit date: 2023-01-19
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 250 ms: 1.03x faster                                           |
| chameleon      | 6.41 ms                                                | 6.31 ms: 1.02x faster                                          |
| docutils       | 2.60 sec                                               | 2.47 sec: 1.05x faster                                         |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                          |
| tornado_http   | 96.6 ms                                                | 93.7 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.7 ms: 1.06x faster                                          |
| nbody          | 95.0 ms                                                | 94.2 ms: 1.01x faster                                          |
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                           |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                           |
| regex_v8       | 22.3 ms                                                | 21.2 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.39 ms: 1.35x faster                                          |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                          |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                          |
| pickle_dict          | 31.4 us                                                | 29.7 us: 1.06x faster                                          |
| pickle_list          | 4.17 us                                                | 4.03 us: 1.04x faster                                          |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                           |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                           |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                          |
| xml_etree_process    | 53.8 ms                                                | 53.6 ms: 1.00x faster                                          |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                   |

Benchmark hidden because not significant (3): unpickle, unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.86 ms: 1.06x slower                                          |
| python_startup_no_site | 5.96 ms                                                | 6.42 ms: 1.08x slower                                          |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text    | 22.1 ms                                                | 21.4 ms: 1.03x faster                                          |
| genshi_xml     | 52.1 ms                                                | 47.3 ms: 1.10x faster                                          |
| mako           | 9.85 ms                                                | 9.59 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 250 ms: 1.03x faster                                           |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.05x faster                                           |
| async_generators        | 359 ms                                                 | 357 ms: 1.00x faster                                           |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                         |
| async_tree_memoization  | 625 ms                                                 | 646 ms: 1.03x slower                                           |
| chameleon               | 6.41 ms                                                | 6.31 ms: 1.02x faster                                          |
| chaos                   | 68.6 ms                                                | 67.9 ms: 1.01x faster                                          |
| bench_thread_pool       | 810 us                                                 | 783 us: 1.03x faster                                           |
| coroutines              | 26.1 ms                                                | 23.2 ms: 1.12x faster                                          |
| coverage                | 101 ms                                                 | 93.9 ms: 1.07x faster                                          |
| crypto_pyaes            | 73.9 ms                                                | 74.5 ms: 1.01x slower                                          |
| deepcopy                | 344 us                                                 | 328 us: 1.05x faster                                           |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                          |
| deepcopy_memo           | 36.4 us                                                | 33.4 us: 1.09x faster                                          |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                          |
| docutils                | 2.60 sec                                               | 2.47 sec: 1.05x faster                                         |
| dulwich_log             | 63.9 ms                                                | 62.0 ms: 1.03x faster                                          |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                           |
| float                   | 76.3 ms                                                | 71.7 ms: 1.06x faster                                          |
| generators              | 72.2 ms                                                | 76.7 ms: 1.06x slower                                          |
| genshi_text             | 22.1 ms                                                | 21.4 ms: 1.03x faster                                          |
| genshi_xml              | 52.1 ms                                                | 47.3 ms: 1.10x faster                                          |
| go                      | 143 ms                                                 | 140 ms: 1.02x faster                                           |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                          |
| hexiom                  | 6.35 ms                                                | 6.03 ms: 1.05x faster                                          |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                          |
| json                    | 4.95 ms                                                | 4.59 ms: 1.08x faster                                          |
| json_dumps              | 12.7 ms                                                | 9.39 ms: 1.35x faster                                          |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                          |
| logging_format          | 6.62 us                                                | 6.34 us: 1.04x faster                                          |
| logging_silent          | 98.5 ns                                                | 91.6 ns: 1.07x faster                                          |
| logging_simple          | 6.06 us                                                | 5.74 us: 1.06x faster                                          |
| mako                    | 9.85 ms                                                | 9.59 ms: 1.03x faster                                          |
| mdp                     | 2.62 sec                                               | 2.52 sec: 1.04x faster                                         |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.02x slower                                           |
| mypy                    | 669 ms                                                 | 810 ms: 1.21x slower                                           |
| nbody                   | 95.0 ms                                                | 94.2 ms: 1.01x faster                                          |
| nqueens                 | 85.0 ms                                                | 77.1 ms: 1.10x faster                                          |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                          |
| pickle_dict             | 31.4 us                                                | 29.7 us: 1.06x faster                                          |
| pickle_list             | 4.17 us                                                | 4.03 us: 1.04x faster                                          |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                           |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                           |
| pprint_safe_repr        | 691 ms                                                 | 663 ms: 1.04x faster                                           |
| pprint_pformat          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                         |
| pycparser               | 1.17 sec                                               | 1.08 sec: 1.08x faster                                         |
| pyflate                 | 417 ms                                                 | 402 ms: 1.04x faster                                           |
| python_startup          | 8.36 ms                                                | 8.86 ms: 1.06x slower                                          |
| python_startup_no_site  | 5.96 ms                                                | 6.42 ms: 1.08x slower                                          |
| raytrace                | 290 ms                                                 | 283 ms: 1.03x faster                                           |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                           |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                           |
| regex_v8                | 22.3 ms                                                | 21.2 ms: 1.05x faster                                          |
| richards                | 46.2 ms                                                | 42.2 ms: 1.09x faster                                          |
| scimark_fft             | 329 ms                                                 | 314 ms: 1.05x faster                                           |
| scimark_monte_carlo     | 68.3 ms                                                | 65.8 ms: 1.04x faster                                          |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                           |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.06 ms: 1.08x faster                                          |
| spectral_norm           | 99.9 ms                                                | 93.8 ms: 1.07x faster                                          |
| sqlglot_parse           | 1.37 ms                                                | 1.39 ms: 1.02x slower                                          |
| sqlglot_transpile       | 1.66 ms                                                | 1.68 ms: 1.01x slower                                          |
| sqlglot_optimize        | 53.0 ms                                                | 50.6 ms: 1.05x faster                                          |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                           |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                          |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                           |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                          |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                           |
| sympy_str               | 287 ms                                                 | 280 ms: 1.03x faster                                           |
| telco                   | 6.62 ms                                                | 6.33 ms: 1.05x faster                                          |
| tornado_http            | 96.6 ms                                                | 93.7 ms: 1.03x faster                                          |
| unpack_sequence         | 43.4 ns                                                | 41.5 ns: 1.05x faster                                          |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                           |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                           |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                          |
| xml_etree_process       | 53.8 ms                                                | 53.6 ms: 1.00x faster                                          |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (11): async_tree_none, async_tree_cpu_io_mixed, bench_mp_pool, django_template, pathlib, regex_effbot, scimark_lu, thrift, unpickle, unpickle_list, xml_etree_iterparse
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230119-3.12.0a4+-a371554/bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
