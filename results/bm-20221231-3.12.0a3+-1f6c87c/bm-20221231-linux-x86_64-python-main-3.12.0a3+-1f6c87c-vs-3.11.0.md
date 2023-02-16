
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 1f6c87c
- commit date: 2022-12-31
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                  |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| html5lib       | 64.8 ms                                                | 60.3 ms: 1.08x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.2 ms: 1.08x faster                                  |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                   |
| nbody          | 90.0 ms                                                | 94.2 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                   |
| regex_effbot   | 3.46 ms                                                | 3.64 ms: 1.05x slower                                  |
| regex_dna      | 203 ms                                                 | 215 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.33 ms: 1.32x faster                                  |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.16x faster                                   |
| json_loads           | 26.1 us                                                | 23.8 us: 1.10x faster                                  |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                   |
| unpickle             | 13.3 us                                                | 12.7 us: 1.05x faster                                  |
| pickle_dict          | 31.2 us                                                | 30.1 us: 1.04x faster                                  |
| pickle_list          | 4.14 us                                                | 4.00 us: 1.04x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| unpickle_list        | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 53.3 ms: 1.01x faster                                  |
| pickle               | 9.90 us                                                | 9.96 us: 1.01x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.4 ms: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.45 ms: 1.01x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.05 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.6 ms: 1.10x faster                                  |
| genshi_text     | 21.5 ms                                                | 20.7 ms: 1.04x faster                                  |
| mako            | 9.83 ms                                                | 9.64 ms: 1.02x faster                                  |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.33 ms: 1.32x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.16x faster                                   |
| deltablue               | 3.66 ms                                                | 3.17 ms: 1.15x faster                                  |
| richards                | 46.1 ms                                                | 41.5 ms: 1.11x faster                                  |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| genshi_xml              | 51.4 ms                                                | 46.6 ms: 1.10x faster                                  |
| json_loads              | 26.1 us                                                | 23.8 us: 1.10x faster                                  |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                   |
| float                   | 76.8 ms                                                | 71.2 ms: 1.08x faster                                  |
| html5lib                | 64.8 ms                                                | 60.3 ms: 1.08x faster                                  |
| logging_silent          | 98.0 ns                                                | 91.4 ns: 1.07x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.30 ms: 1.07x faster                                  |
| nqueens                 | 83.8 ms                                                | 78.9 ms: 1.06x faster                                  |
| unpack_sequence         | 44.5 ns                                                | 42.0 ns: 1.06x faster                                  |
| logging_simple          | 6.02 us                                                | 5.72 us: 1.05x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.5 ms: 1.05x faster                                  |
| bench_thread_pool       | 817 us                                                 | 777 us: 1.05x faster                                   |
| hexiom                  | 6.34 ms                                                | 6.04 ms: 1.05x faster                                  |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                  |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                  |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                   |
| unpickle                | 13.3 us                                                | 12.7 us: 1.05x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                 |
| spectral_norm           | 98.1 ms                                                | 94.1 ms: 1.04x faster                                  |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                   |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                   |
| sqlglot_optimize        | 52.7 ms                                                | 50.7 ms: 1.04x faster                                  |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                  |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| telco                   | 6.43 ms                                                | 6.19 ms: 1.04x faster                                  |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| scimark_fft             | 325 ms                                                 | 314 ms: 1.04x faster                                   |
| pickle_dict             | 31.2 us                                                | 30.1 us: 1.04x faster                                  |
| pickle_list             | 4.14 us                                                | 4.00 us: 1.04x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| coroutines              | 26.2 ms                                                | 25.5 ms: 1.03x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                 |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                  |
| dulwich_log             | 64.0 ms                                                | 62.4 ms: 1.02x faster                                  |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.02x faster                                   |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| mako                    | 9.83 ms                                                | 9.64 ms: 1.02x faster                                  |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pprint_safe_repr        | 706 ms                                                 | 694 ms: 1.02x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 74.4 ms: 1.02x faster                                  |
| python_startup          | 8.58 ms                                                | 8.45 ms: 1.01x faster                                  |
| thrift                  | 760 us                                                 | 749 us: 1.01x faster                                   |
| chaos                   | 68.7 ms                                                | 68.0 ms: 1.01x faster                                  |
| deepcopy                | 341 us                                                 | 338 us: 1.01x faster                                   |
| async_generators        | 356 ms                                                 | 352 ms: 1.01x faster                                   |
| unpickle_list           | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| xml_etree_process       | 53.7 ms                                                | 53.3 ms: 1.01x faster                                  |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.05 ms: 1.00x slower                                  |
| pickle                  | 9.90 us                                                | 9.96 us: 1.01x slower                                  |
| mdp                     | 2.63 sec                                               | 2.64 sec: 1.01x slower                                 |
| xml_etree_generate      | 75.9 ms                                                | 76.4 ms: 1.01x slower                                  |
| pathlib                 | 18.1 ms                                                | 18.2 ms: 1.01x slower                                  |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| coverage                | 99.3 ms                                                | 100 ms: 1.01x slower                                   |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 751 ms: 1.02x slower                                   |
| sqlglot_parse           | 1.36 ms                                                | 1.39 ms: 1.02x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.03x slower                                  |
| generators              | 73.5 ms                                                | 76.4 ms: 1.04x slower                                  |
| nbody                   | 90.0 ms                                                | 94.2 ms: 1.05x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.64 ms: 1.05x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                  |
| regex_dna               | 203 ms                                                 | 215 ms: 1.06x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): djangocms, async_tree_memoization, logging_format, async_tree_none, regex_v8, bench_mp_pool, scimark_lu
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221231-3.12.0a3+-1f6c87c/bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c.json: mypy
