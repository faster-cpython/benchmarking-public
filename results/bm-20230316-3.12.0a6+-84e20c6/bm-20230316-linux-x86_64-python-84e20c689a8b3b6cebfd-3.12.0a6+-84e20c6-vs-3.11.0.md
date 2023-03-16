
# Results vs. 3.11.0

- fork: python
- ref: 84e20c689a8b3b6cebfd
- machine: linux-x86_64
- commit hash: 84e20c6
- commit date: 2023-03-16
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                   |
| chameleon      | 6.38 ms                                                | 6.47 ms: 1.01x slower                                                  |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| html5lib       | 64.8 ms                                                | 60.7 ms: 1.07x faster                                                  |
| tornado_http   | 96.5 ms                                                | 91.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                  |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                   |
| nbody          | 90.0 ms                                                | 88.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                  |
| regex_compile  | 136 ms                                                 | 133 ms: 1.02x faster                                                   |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                                   |
| regex_effbot   | 3.46 ms                                                | 3.62 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 280 us: 1.10x faster                                                   |
| json_loads           | 26.1 us                                                | 24.0 us: 1.08x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 98.5 ms: 1.06x faster                                                  |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.01x faster                                                  |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| pickle_list          | 4.14 us                                                | 4.28 us: 1.03x slower                                                  |
| xml_etree_process    | 53.7 ms                                                | 56.1 ms: 1.05x slower                                                  |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 81.1 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.93 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.5 ms: 1.08x faster                                                  |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                  |
| django_template | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.5 ms: 2.49x faster                                                  |
| asyncio_tcp             | 883 ms                                                 | 507 ms: 1.74x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                   |
| deltablue               | 3.66 ms                                                | 3.15 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                   |
| coroutines              | 26.2 ms                                                | 23.1 ms: 1.13x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.17 ms: 1.10x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 280 us: 1.10x faster                                                   |
| richards                | 46.1 ms                                                | 42.0 ms: 1.10x faster                                                  |
| json_loads              | 26.1 us                                                | 24.0 us: 1.08x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.08x faster                                                 |
| mdp                     | 2.63 sec                                               | 2.43 sec: 1.08x faster                                                 |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                   |
| genshi_xml              | 51.4 ms                                                | 47.5 ms: 1.08x faster                                                  |
| deepcopy_memo           | 35.8 us                                                | 33.1 us: 1.08x faster                                                  |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                   |
| logging_simple          | 6.02 us                                                | 5.62 us: 1.07x faster                                                  |
| html5lib                | 64.8 ms                                                | 60.7 ms: 1.07x faster                                                  |
| scimark_fft             | 325 ms                                                 | 306 ms: 1.07x faster                                                   |
| spectral_norm           | 98.1 ms                                                | 92.3 ms: 1.06x faster                                                  |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                   |
| tornado_http            | 96.5 ms                                                | 91.0 ms: 1.06x faster                                                  |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 98.5 ms: 1.06x faster                                                  |
| coverage                | 99.3 ms                                                | 94.2 ms: 1.05x faster                                                  |
| deepcopy                | 341 us                                                 | 324 us: 1.05x faster                                                   |
| raytrace                | 291 ms                                                 | 278 ms: 1.05x faster                                                   |
| logging_silent          | 98.0 ns                                                | 93.4 ns: 1.05x faster                                                  |
| nqueens                 | 83.8 ms                                                | 79.9 ms: 1.05x faster                                                  |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                                   |
| float                   | 76.8 ms                                                | 73.7 ms: 1.04x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                 |
| logging_format          | 6.48 us                                                | 6.22 us: 1.04x faster                                                  |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                  |
| gc_traversal            | 3.82 ms                                                | 3.67 ms: 1.04x faster                                                  |
| chaos                   | 68.7 ms                                                | 66.0 ms: 1.04x faster                                                  |
| hexiom                  | 6.34 ms                                                | 6.10 ms: 1.04x faster                                                  |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                                  |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.04x faster                                                   |
| pprint_safe_repr        | 706 ms                                                 | 682 ms: 1.04x faster                                                   |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                                  |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                  |
| bench_thread_pool       | 817 us                                                 | 791 us: 1.03x faster                                                   |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 66.0 ms: 1.03x faster                                                  |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                                   |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                  |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.03x faster                                                 |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                  |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.02x faster                                                  |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                   |
| regex_compile           | 136 ms                                                 | 133 ms: 1.02x faster                                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                   |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                                   |
| pyflate                 | 419 ms                                                 | 412 ms: 1.02x faster                                                   |
| async_tree_none         | 526 ms                                                 | 518 ms: 1.02x faster                                                   |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                                  |
| async_tree_memoization  | 624 ms                                                 | 614 ms: 1.02x faster                                                   |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                  |
| nbody                   | 90.0 ms                                                | 88.8 ms: 1.01x faster                                                  |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| crypto_pyaes            | 75.7 ms                                                | 75.1 ms: 1.01x faster                                                  |
| unpack_sequence         | 44.5 ns                                                | 44.2 ns: 1.01x faster                                                  |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.01x faster                                                  |
| thrift                  | 760 us                                                 | 769 us: 1.01x slower                                                   |
| chameleon               | 6.38 ms                                                | 6.47 ms: 1.01x slower                                                  |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                  |
| pickle_list             | 4.14 us                                                | 4.28 us: 1.03x slower                                                  |
| django_template         | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                  |
| python_startup          | 8.58 ms                                                | 8.93 ms: 1.04x slower                                                  |
| xml_etree_process       | 53.7 ms                                                | 56.1 ms: 1.05x slower                                                  |
| regex_effbot            | 3.46 ms                                                | 3.62 ms: 1.05x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                                  |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                                  |
| xml_etree_generate      | 75.9 ms                                                | 81.1 ms: 1.07x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                  |
| async_generators        | 356 ms                                                 | 410 ms: 1.15x slower                                                   |
| dask                    | 365 ms                                                 | 500 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (8): unpickle, djangocms, sympy_sum, genshi_text, async_tree_cpu_io_mixed, bench_mp_pool, telco, scimark_lu
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-84e20c6/bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6.json: comprehensions
