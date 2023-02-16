
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 6b312e0
- commit date: 2023-02-03
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| chameleon      | 6.38 ms                                                | 6.28 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 59.5 ms: 1.09x faster                                               |
| tornado_http   | 96.5 ms                                                | 94.0 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                               |
| pidigits       | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| nbody          | 90.0 ms                                                | 96.7 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| regex_v8       | 22.2 ms                                                | 22.6 ms: 1.02x slower                                               |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.52 ms: 1.30x faster                                               |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.14x faster                                                |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.08x faster                                                |
| pickle_list          | 4.14 us                                                | 3.92 us: 1.06x faster                                               |
| pickle_dict          | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| xml_etree_process    | 53.7 ms                                                | 53.4 ms: 1.01x faster                                               |
| unpickle_list        | 4.99 us                                                | 5.02 us: 1.01x slower                                               |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 77.6 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.48 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.9 ms: 1.07x faster                                               |
| genshi_text    | 21.5 ms                                                | 20.8 ms: 1.04x faster                                               |
| mako           | 9.83 ms                                                | 9.58 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.52 ms: 1.30x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.98 ms: 1.15x faster                                               |
| deltablue               | 3.66 ms                                                | 3.18 ms: 1.15x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.14x faster                                                |
| nqueens                 | 83.8 ms                                                | 75.8 ms: 1.11x faster                                               |
| richards                | 46.1 ms                                                | 41.8 ms: 1.10x faster                                               |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                               |
| html5lib                | 64.8 ms                                                | 59.5 ms: 1.09x faster                                               |
| gc_traversal            | 3.82 ms                                                | 3.52 ms: 1.08x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| chaos                   | 68.7 ms                                                | 63.5 ms: 1.08x faster                                               |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.08x faster                                                |
| genshi_xml              | 51.4 ms                                                | 47.9 ms: 1.07x faster                                               |
| mdp                     | 2.63 sec                                               | 2.45 sec: 1.07x faster                                              |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| hexiom                  | 6.34 ms                                                | 5.94 ms: 1.07x faster                                               |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                               |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                              |
| pickle_list             | 4.14 us                                                | 3.92 us: 1.06x faster                                               |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                                |
| logging_silent          | 98.0 ns                                                | 92.7 ns: 1.06x faster                                               |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                                |
| logging_simple          | 6.02 us                                                | 5.70 us: 1.06x faster                                               |
| deepcopy                | 341 us                                                 | 324 us: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                               |
| deepcopy_reduce         | 3.02 us                                                | 2.88 us: 1.05x faster                                               |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                              |
| pickle_dict             | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                |
| bench_thread_pool       | 817 us                                                 | 784 us: 1.04x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                               |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.04x faster                                               |
| pidigits                | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                               |
| logging_format          | 6.48 us                                                | 6.28 us: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| async_generators        | 356 ms                                                 | 346 ms: 1.03x faster                                                |
| dulwich_log             | 64.0 ms                                                | 62.3 ms: 1.03x faster                                               |
| tornado_http            | 96.5 ms                                                | 94.0 ms: 1.03x faster                                               |
| mako                    | 9.83 ms                                                | 9.58 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| fannkuch                | 384 ms                                                 | 375 ms: 1.02x faster                                                |
| raytrace                | 291 ms                                                 | 285 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 68.0 ms                                                | 66.5 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| thrift                  | 760 us                                                 | 747 us: 1.02x faster                                                |
| chameleon               | 6.38 ms                                                | 6.28 ms: 1.02x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                               |
| pyflate                 | 419 ms                                                 | 414 ms: 1.01x faster                                                |
| xml_etree_process       | 53.7 ms                                                | 53.4 ms: 1.01x faster                                               |
| coroutines              | 26.2 ms                                                | 26.0 ms: 1.01x faster                                               |
| unpickle_list           | 4.99 us                                                | 5.02 us: 1.01x slower                                               |
| crypto_pyaes            | 75.7 ms                                                | 76.4 ms: 1.01x slower                                               |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                               |
| generators              | 73.5 ms                                                | 74.5 ms: 1.01x slower                                               |
| regex_v8                | 22.2 ms                                                | 22.6 ms: 1.02x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.53 us: 1.02x slower                                               |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| xml_etree_generate      | 75.9 ms                                                | 77.6 ms: 1.02x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.03x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 760 ms: 1.03x slower                                                |
| async_tree_memoization  | 624 ms                                                 | 652 ms: 1.04x slower                                                |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.04x slower                                               |
| spectral_norm           | 98.1 ms                                                | 103 ms: 1.05x slower                                                |
| unpack_sequence         | 44.5 ns                                                | 46.9 ns: 1.06x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.48 ms: 1.07x slower                                               |
| nbody                   | 90.0 ms                                                | 96.7 ms: 1.07x slower                                               |
| dask                    | 365 ms                                                 | 499 ms: 1.37x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (10): unpickle, djangocms, regex_effbot, django_template, scimark_lu, bench_mp_pool, meteor_contest, async_tree_none, telco, coverage
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-6b312e0/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0.json: mypy
