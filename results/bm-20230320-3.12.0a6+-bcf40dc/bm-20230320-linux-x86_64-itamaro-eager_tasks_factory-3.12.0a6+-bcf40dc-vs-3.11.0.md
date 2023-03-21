
# Results vs. 3.11.0

- fork: itamaro
- ref: eager_tasks_factory
- machine: linux-x86_64
- commit hash: bcf40dc
- commit date: 2023-03-20
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                   |
| chameleon      | 6.38 ms                                                | 6.27 ms: 1.02x faster                                                  |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| html5lib       | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.0 ms: 1.04x faster                                                  |
| nbody          | 90.0 ms                                                | 87.6 ms: 1.03x faster                                                  |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.30 ms: 1.05x faster                                                  |
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                                   |
| regex_v8       | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                  |
| regex_dna      | 203 ms                                                 | 204 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                                   |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pickle_dict          | 31.2 us                                                | 31.3 us: 1.00x slower                                                  |
| pickle_list          | 4.14 us                                                | 4.21 us: 1.02x slower                                                  |
| xml_etree_process    | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 80.1 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.55 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.8 ms: 1.08x faster                                                  |
| genshi_text     | 21.5 ms                                                | 21.0 ms: 1.02x faster                                                  |
| mako            | 9.83 ms                                                | 9.99 ms: 1.02x slower                                                  |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                                  |
| asyncio_tcp             | 883 ms                                                 | 506 ms: 1.74x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                   |
| coroutines              | 26.2 ms                                                | 22.4 ms: 1.17x faster                                                  |
| deltablue               | 3.66 ms                                                | 3.14 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                   |
| spectral_norm           | 98.1 ms                                                | 88.2 ms: 1.11x faster                                                  |
| richards                | 46.1 ms                                                | 42.0 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.18 ms: 1.10x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                                   |
| scimark_fft             | 325 ms                                                 | 297 ms: 1.09x faster                                                   |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                   |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| genshi_xml              | 51.4 ms                                                | 47.8 ms: 1.08x faster                                                  |
| nqueens                 | 83.8 ms                                                | 78.2 ms: 1.07x faster                                                  |
| html5lib                | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                 |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                                  |
| deepcopy                | 341 us                                                 | 323 us: 1.06x faster                                                   |
| logging_simple          | 6.02 us                                                | 5.69 us: 1.06x faster                                                  |
| deepcopy_memo           | 35.8 us                                                | 34.0 us: 1.05x faster                                                  |
| fannkuch                | 384 ms                                                 | 365 ms: 1.05x faster                                                   |
| chaos                   | 68.7 ms                                                | 65.5 ms: 1.05x faster                                                  |
| regex_effbot            | 3.46 ms                                                | 3.30 ms: 1.05x faster                                                  |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                   |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| hexiom                  | 6.34 ms                                                | 6.08 ms: 1.04x faster                                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                  |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                   |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                   |
| logging_format          | 6.48 us                                                | 6.23 us: 1.04x faster                                                  |
| pyflate                 | 419 ms                                                 | 403 ms: 1.04x faster                                                   |
| float                   | 76.8 ms                                                | 74.0 ms: 1.04x faster                                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 65.5 ms: 1.04x faster                                                  |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                 |
| unpack_sequence         | 44.5 ns                                                | 42.9 ns: 1.04x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 73.2 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                  |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                                   |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                  |
| mdp                     | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| pprint_safe_repr        | 706 ms                                                 | 687 ms: 1.03x faster                                                   |
| nbody                   | 90.0 ms                                                | 87.6 ms: 1.03x faster                                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                                  |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                  |
| coverage                | 99.3 ms                                                | 96.8 ms: 1.03x faster                                                  |
| raytrace                | 291 ms                                                 | 284 ms: 1.02x faster                                                   |
| genshi_text             | 21.5 ms                                                | 21.0 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                   |
| logging_silent          | 98.0 ns                                                | 96.2 ns: 1.02x faster                                                  |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                                  |
| chameleon               | 6.38 ms                                                | 6.27 ms: 1.02x faster                                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.01x faster                                                  |
| telco                   | 6.43 ms                                                | 6.36 ms: 1.01x faster                                                  |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                   |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                 |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| sympy_sum               | 166 ms                                                 | 165 ms: 1.01x faster                                                   |
| regex_v8                | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                  |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| pickle_dict             | 31.2 us                                                | 31.3 us: 1.00x slower                                                  |
| regex_dna               | 203 ms                                                 | 204 ms: 1.01x slower                                                   |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                   |
| mako                    | 9.83 ms                                                | 9.99 ms: 1.02x slower                                                  |
| pickle_list             | 4.14 us                                                | 4.21 us: 1.02x slower                                                  |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                  |
| xml_etree_process       | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                  |
| thrift                  | 760 us                                                 | 788 us: 1.04x slower                                                   |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                  |
| gc_traversal            | 3.82 ms                                                | 3.98 ms: 1.04x slower                                                  |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                  |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| xml_etree_generate      | 75.9 ms                                                | 80.1 ms: 1.06x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.55 ms: 1.09x slower                                                  |
| async_generators        | 356 ms                                                 | 411 ms: 1.16x slower                                                   |
| dask                    | 365 ms                                                 | 499 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): djangocms, async_tree_memoization, unpickle_list, bench_mp_pool, async_tree_cpu_io_mixed, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230320-3.12.0a6+-bcf40dc/bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc.json: comprehensions
