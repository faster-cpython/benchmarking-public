
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: dec1ab0
- commit date: 2023-02-07
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 254 ms: 1.01x faster                                   |
| chameleon      | 6.41 ms                                                | 6.27 ms: 1.02x faster                                  |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| html5lib       | 63.2 ms                                                | 60.8 ms: 1.04x faster                                  |
| tornado_http   | 96.6 ms                                                | 94.6 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.1 ms: 1.06x faster                                  |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                   |
| regex_v8       | 22.3 ms                                                | 21.9 ms: 1.02x faster                                  |
| regex_effbot   | 3.36 ms                                                | 3.44 ms: 1.03x slower                                  |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.41 ms: 1.35x faster                                  |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                   |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| pickle_pure_python   | 304 us                                                 | 286 us: 1.06x faster                                   |
| pickle_dict          | 31.4 us                                                | 31.2 us: 1.01x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 77.3 ms: 1.01x slower                                  |
| unpickle_list        | 4.95 us                                                | 5.04 us: 1.02x slower                                  |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (4): unpickle, xml_etree_iterparse, pickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.97 ms: 1.07x slower                                  |
| python_startup_no_site | 5.96 ms                                                | 6.49 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.7 ms: 1.12x faster                                  |
| genshi_text     | 22.1 ms                                                | 20.4 ms: 1.08x faster                                  |
| mako            | 9.85 ms                                                | 9.72 ms: 1.01x faster                                  |
| django_template | 32.5 ms                                                | 33.5 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.41 ms: 1.35x faster                                  |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                   |
| genshi_xml              | 52.1 ms                                                | 46.7 ms: 1.12x faster                                  |
| richards                | 46.2 ms                                                | 41.8 ms: 1.11x faster                                  |
| deltablue               | 3.64 ms                                                | 3.30 ms: 1.11x faster                                  |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.01 ms: 1.10x faster                                  |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                  |
| genshi_text             | 22.1 ms                                                | 20.4 ms: 1.08x faster                                  |
| nqueens                 | 85.0 ms                                                | 78.8 ms: 1.08x faster                                  |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                   |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                   |
| json                    | 4.95 ms                                                | 4.62 ms: 1.07x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| scimark_fft             | 329 ms                                                 | 308 ms: 1.07x faster                                   |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                   |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.06x faster                                  |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                   |
| pickle_pure_python      | 304 us                                                 | 286 us: 1.06x faster                                   |
| hexiom                  | 6.35 ms                                                | 5.99 ms: 1.06x faster                                  |
| float                   | 76.3 ms                                                | 72.1 ms: 1.06x faster                                  |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                  |
| coverage                | 101 ms                                                 | 95.3 ms: 1.05x faster                                  |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                   |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                   |
| deepcopy                | 344 us                                                 | 327 us: 1.05x faster                                   |
| logging_silent          | 98.5 ns                                                | 93.8 ns: 1.05x faster                                  |
| logging_simple          | 6.06 us                                                | 5.78 us: 1.05x faster                                  |
| chaos                   | 68.6 ms                                                | 65.5 ms: 1.05x faster                                  |
| pyflate                 | 417 ms                                                 | 399 ms: 1.04x faster                                   |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                  |
| go                      | 143 ms                                                 | 138 ms: 1.04x faster                                   |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| html5lib                | 63.2 ms                                                | 60.8 ms: 1.04x faster                                  |
| telco                   | 6.62 ms                                                | 6.38 ms: 1.04x faster                                  |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| bench_thread_pool       | 810 us                                                 | 781 us: 1.04x faster                                   |
| coroutines              | 26.1 ms                                                | 25.2 ms: 1.04x faster                                  |
| spectral_norm           | 99.9 ms                                                | 96.5 ms: 1.04x faster                                  |
| logging_format          | 6.62 us                                                | 6.39 us: 1.04x faster                                  |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.02x faster                                  |
| chameleon               | 6.41 ms                                                | 6.27 ms: 1.02x faster                                  |
| tornado_http            | 96.6 ms                                                | 94.6 ms: 1.02x faster                                  |
| pprint_pformat          | 1.44 sec                                               | 1.42 sec: 1.02x faster                                 |
| regex_v8                | 22.3 ms                                                | 21.9 ms: 1.02x faster                                  |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                 |
| 2to3                    | 257 ms                                                 | 254 ms: 1.01x faster                                   |
| mako                    | 9.85 ms                                                | 9.72 ms: 1.01x faster                                  |
| dulwich_log             | 63.9 ms                                                | 63.1 ms: 1.01x faster                                  |
| raytrace                | 290 ms                                                 | 287 ms: 1.01x faster                                   |
| sqlalchemy_declarative  | 139 ms                                                 | 137 ms: 1.01x faster                                   |
| async_generators        | 359 ms                                                 | 356 ms: 1.01x faster                                   |
| pickle_dict             | 31.4 us                                                | 31.2 us: 1.01x faster                                  |
| pprint_safe_repr        | 691 ms                                                 | 695 ms: 1.01x slower                                   |
| crypto_pyaes            | 73.9 ms                                                | 74.4 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 752 ms                                                 | 760 ms: 1.01x slower                                   |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                 |
| xml_etree_generate      | 76.2 ms                                                | 77.3 ms: 1.01x slower                                  |
| unpickle_list           | 4.95 us                                                | 5.04 us: 1.02x slower                                  |
| regex_effbot            | 3.36 ms                                                | 3.44 ms: 1.03x slower                                  |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                  |
| unpack_sequence         | 43.4 ns                                                | 44.7 ns: 1.03x slower                                  |
| django_template         | 32.5 ms                                                | 33.5 ms: 1.03x slower                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.03x slower                                  |
| thrift                  | 752 us                                                 | 777 us: 1.03x slower                                   |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                  |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                   |
| mdp                     | 2.62 sec                                               | 2.73 sec: 1.04x slower                                 |
| generators              | 72.2 ms                                                | 76.8 ms: 1.06x slower                                  |
| async_tree_memoization  | 625 ms                                                 | 665 ms: 1.06x slower                                   |
| python_startup          | 8.36 ms                                                | 8.97 ms: 1.07x slower                                  |
| python_startup_no_site  | 5.96 ms                                                | 6.49 ms: 1.09x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (12): unpickle, async_tree_none, meteor_contest, scimark_monte_carlo, xml_etree_iterparse, pickle_list, bench_mp_pool, deepcopy_reduce, xml_etree_process, sqlalchemy_imperative, nbody, scimark_lu
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (6) of /home/mdboom/Work/builds/benchmarking/results/bm-20230207-3.12.0a4+-dec1ab0/bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
