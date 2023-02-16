
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c1c5882
- commit date: 2023-01-21
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                   |
| chameleon      | 6.38 ms                                                | 6.32 ms: 1.01x faster                                  |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                 |
| html5lib       | 64.8 ms                                                | 60.8 ms: 1.07x faster                                  |
| tornado_http   | 96.5 ms                                                | 93.9 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.0 ms: 1.07x faster                                  |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| nbody          | 90.0 ms                                                | 92.7 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                  |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.65 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.39 ms: 1.32x faster                                  |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                   |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                   |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                  |
| pickle_list          | 4.14 us                                                | 4.01 us: 1.03x faster                                  |
| pickle_dict          | 31.2 us                                                | 30.3 us: 1.03x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 159 ms: 1.01x faster                                   |
| unpickle_list        | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| xml_etree_process    | 53.7 ms                                                | 54.1 ms: 1.01x slower                                  |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| xml_etree_generate   | 75.9 ms                                                | 78.1 ms: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.95 ms: 1.04x slower                                  |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.3 ms: 1.09x faster                                  |
| genshi_text    | 21.5 ms                                                | 21.1 ms: 1.02x faster                                  |
| mako           | 9.83 ms                                                | 9.90 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 502 ms: 1.76x faster                                   |
| json_dumps              | 12.4 ms                                                | 9.39 ms: 1.32x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.97 ms: 1.16x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                   |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                  |
| nqueens                 | 83.8 ms                                                | 76.0 ms: 1.10x faster                                  |
| chaos                   | 68.7 ms                                                | 62.4 ms: 1.10x faster                                  |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                   |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                   |
| genshi_xml              | 51.4 ms                                                | 47.3 ms: 1.09x faster                                  |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                  |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                   |
| hexiom                  | 6.34 ms                                                | 5.88 ms: 1.08x faster                                  |
| richards                | 46.1 ms                                                | 42.9 ms: 1.08x faster                                  |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| mdp                     | 2.63 sec                                               | 2.46 sec: 1.07x faster                                 |
| float                   | 76.8 ms                                                | 72.0 ms: 1.07x faster                                  |
| html5lib                | 64.8 ms                                                | 60.8 ms: 1.07x faster                                  |
| unpack_sequence         | 44.5 ns                                                | 41.7 ns: 1.07x faster                                  |
| logging_silent          | 98.0 ns                                                | 92.0 ns: 1.07x faster                                  |
| coroutines              | 26.2 ms                                                | 24.6 ms: 1.07x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 665 ms: 1.06x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                 |
| fannkuch                | 384 ms                                                 | 364 ms: 1.06x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.5 ms: 1.05x faster                                  |
| aiohttp                 | 1.05 ms                                                | 996 us: 1.05x faster                                   |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                   |
| pyflate                 | 419 ms                                                 | 398 ms: 1.05x faster                                   |
| deepcopy                | 341 us                                                 | 325 us: 1.05x faster                                   |
| bench_thread_pool       | 817 us                                                 | 781 us: 1.05x faster                                   |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 72.8 ms: 1.04x faster                                  |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                  |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                 |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                   |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.04x faster                                 |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                  |
| coverage                | 99.3 ms                                                | 96.0 ms: 1.03x faster                                  |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| pickle_list             | 4.14 us                                                | 4.01 us: 1.03x faster                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                  |
| logging_simple          | 6.02 us                                                | 5.84 us: 1.03x faster                                  |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                   |
| json                    | 4.87 ms                                                | 4.73 ms: 1.03x faster                                  |
| tornado_http            | 96.5 ms                                                | 93.9 ms: 1.03x faster                                  |
| pickle_dict             | 31.2 us                                                | 30.3 us: 1.03x faster                                  |
| spectral_norm           | 98.1 ms                                                | 95.8 ms: 1.02x faster                                  |
| async_generators        | 356 ms                                                 | 347 ms: 1.02x faster                                   |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| dulwich_log             | 64.0 ms                                                | 62.5 ms: 1.02x faster                                  |
| genshi_text             | 21.5 ms                                                | 21.1 ms: 1.02x faster                                  |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                   |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                  |
| thrift                  | 760 us                                                 | 744 us: 1.02x faster                                   |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                  |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.01x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 159 ms: 1.01x faster                                   |
| chameleon               | 6.38 ms                                                | 6.32 ms: 1.01x faster                                  |
| unpickle_list           | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| mako                    | 9.83 ms                                                | 9.90 ms: 1.01x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 54.1 ms: 1.01x slower                                  |
| meteor_contest          | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                  |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                 |
| gc_traversal            | 3.82 ms                                                | 3.88 ms: 1.02x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 78.1 ms: 1.03x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                  |
| nbody                   | 90.0 ms                                                | 92.7 ms: 1.03x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 645 ms: 1.03x slower                                   |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                   |
| generators              | 73.5 ms                                                | 76.6 ms: 1.04x slower                                  |
| python_startup          | 8.58 ms                                                | 8.95 ms: 1.04x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.65 ms: 1.06x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.07x slower                                  |
| dask                    | 365 ms                                                 | 497 ms: 1.36x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (6): telco, djangocms, django_template, bench_mp_pool, async_tree_none, unpickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230121-3.12.0a4+-c1c5882/bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882.json: mypy
