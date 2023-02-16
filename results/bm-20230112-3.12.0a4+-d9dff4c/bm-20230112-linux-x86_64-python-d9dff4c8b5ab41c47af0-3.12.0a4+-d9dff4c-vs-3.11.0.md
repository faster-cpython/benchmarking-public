
# Results vs. 3.11.0

- fork: python
- ref: d9dff4c8b5ab41c47af0
- machine: linux-x86_64
- commit hash: d9dff4c
- commit date: 2023-01-12
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.4 ms: 1.06x faster                                                  |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                                   |
| nbody          | 90.0 ms                                                | 94.4 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                  |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                                   |
| regex_effbot   | 3.46 ms                                                | 3.61 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.39 ms: 1.32x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                   |
| json_loads           | 26.1 us                                                | 23.6 us: 1.10x faster                                                  |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                                   |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                   |
| pickle_list          | 4.14 us                                                | 4.04 us: 1.03x faster                                                  |
| unpickle             | 13.3 us                                                | 12.9 us: 1.02x faster                                                  |
| pickle_dict          | 31.2 us                                                | 30.4 us: 1.02x faster                                                  |
| xml_etree_process    | 53.7 ms                                                | 53.3 ms: 1.01x faster                                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.58 ms: 1.00x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.13 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                  |
| genshi_text     | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                  |
| mako            | 9.83 ms                                                | 9.77 ms: 1.01x faster                                                  |
| django_template | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 505 ms: 1.75x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.39 ms: 1.32x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                   |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                                  |
| richards                | 46.1 ms                                                | 41.3 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.11 ms: 1.12x faster                                                  |
| json_loads              | 26.1 us                                                | 23.6 us: 1.10x faster                                                  |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                                   |
| logging_silent          | 98.0 ns                                                | 89.8 ns: 1.09x faster                                                  |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                  |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                   |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                   |
| float                   | 76.8 ms                                                | 72.4 ms: 1.06x faster                                                  |
| genshi_text             | 21.5 ms                                                | 20.3 ms: 1.06x faster                                                  |
| coroutines              | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                  |
| deepcopy_memo           | 35.8 us                                                | 33.8 us: 1.06x faster                                                  |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 64.5 ms: 1.05x faster                                                  |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                                  |
| bench_thread_pool       | 817 us                                                 | 776 us: 1.05x faster                                                   |
| mdp                     | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                 |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 673 ms: 1.05x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| sqlglot_optimize        | 52.7 ms                                                | 50.3 ms: 1.05x faster                                                  |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                                   |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                   |
| nqueens                 | 83.8 ms                                                | 80.3 ms: 1.04x faster                                                  |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                   |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                                   |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                  |
| json                    | 4.87 ms                                                | 4.70 ms: 1.04x faster                                                  |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                 |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                   |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                                   |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                   |
| chaos                   | 68.7 ms                                                | 66.8 ms: 1.03x faster                                                  |
| dulwich_log             | 64.0 ms                                                | 62.3 ms: 1.03x faster                                                  |
| pickle_list             | 4.14 us                                                | 4.04 us: 1.03x faster                                                  |
| unpickle                | 13.3 us                                                | 12.9 us: 1.02x faster                                                  |
| pickle_dict             | 31.2 us                                                | 30.4 us: 1.02x faster                                                  |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                  |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                                   |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                   |
| telco                   | 6.43 ms                                                | 6.33 ms: 1.01x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.8 ms: 1.01x faster                                                  |
| spectral_norm           | 98.1 ms                                                | 97.1 ms: 1.01x faster                                                  |
| logging_format          | 6.48 us                                                | 6.42 us: 1.01x faster                                                  |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                  |
| xml_etree_process       | 53.7 ms                                                | 53.3 ms: 1.01x faster                                                  |
| mako                    | 9.83 ms                                                | 9.77 ms: 1.01x faster                                                  |
| thrift                  | 760 us                                                 | 755 us: 1.01x faster                                                   |
| gc_traversal            | 3.82 ms                                                | 3.80 ms: 1.00x faster                                                  |
| async_generators        | 356 ms                                                 | 355 ms: 1.00x faster                                                   |
| python_startup          | 8.58 ms                                                | 8.58 ms: 1.00x slower                                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                  |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                  |
| unpack_sequence         | 44.5 ns                                                | 45.1 ns: 1.01x slower                                                  |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.13 ms: 1.02x slower                                                  |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| coverage                | 99.3 ms                                                | 101 ms: 1.02x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                  |
| django_template         | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.39 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 754 ms: 1.03x slower                                                   |
| generators              | 73.5 ms                                                | 75.4 ms: 1.03x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.57 us: 1.04x slower                                                  |
| regex_effbot            | 3.46 ms                                                | 3.61 ms: 1.04x slower                                                  |
| nbody                   | 90.0 ms                                                | 94.4 ms: 1.05x slower                                                  |
| async_tree_memoization  | 624 ms                                                 | 657 ms: 1.05x slower                                                   |
| dask                    | 365 ms                                                 | 495 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (6): djangocms, unpickle_list, bench_mp_pool, chameleon, async_tree_none, scimark_lu
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230112-3.12.0a4+-d9dff4c/bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c.json: mypy
