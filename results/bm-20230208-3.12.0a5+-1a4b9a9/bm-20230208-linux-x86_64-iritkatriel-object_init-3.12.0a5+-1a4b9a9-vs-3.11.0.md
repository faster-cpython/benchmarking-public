
# Results vs. 3.11.0

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 1a4b9a9
- commit date: 2023-02-08
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                               |
| docutils       | 2.60 sec                                               | 2.56 sec: 1.02x faster                                             |
| html5lib       | 64.8 ms                                                | 60.9 ms: 1.06x faster                                              |
| tornado_http   | 96.5 ms                                                | 94.0 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.1 ms: 1.07x faster                                              |
| nbody          | 90.0 ms                                                | 86.0 ms: 1.05x faster                                              |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                               |
| regex_effbot   | 3.46 ms                                                | 3.32 ms: 1.04x faster                                              |
| regex_v8       | 22.2 ms                                                | 21.4 ms: 1.04x faster                                              |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.34 ms: 1.32x faster                                              |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                               |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                               |
| pickle_pure_python   | 308 us                                                 | 288 us: 1.07x faster                                               |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                              |
| pickle_list          | 4.14 us                                                | 4.09 us: 1.01x faster                                              |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                              |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| xml_etree_process    | 53.7 ms                                                | 55.6 ms: 1.04x slower                                              |
| xml_etree_iterparse  | 104 ms                                                 | 108 ms: 1.04x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 81.3 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                              |
| python_startup_no_site | 6.04 ms                                                | 6.51 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 46.4 ms: 1.11x faster                                              |
| genshi_text    | 21.5 ms                                                | 20.7 ms: 1.04x faster                                              |
| mako           | 9.83 ms                                                | 9.65 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 490 ms: 1.80x faster                                               |
| json_dumps              | 12.4 ms                                                | 9.34 ms: 1.32x faster                                              |
| mypy2                   | 420 ms                                                 | 328 ms: 1.28x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.90 ms: 1.18x faster                                              |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                               |
| deltablue               | 3.66 ms                                                | 3.18 ms: 1.15x faster                                              |
| genshi_xml              | 51.4 ms                                                | 46.4 ms: 1.11x faster                                              |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                              |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                              |
| scimark_fft             | 325 ms                                                 | 298 ms: 1.09x faster                                               |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                             |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                               |
| sympy_str               | 291 ms                                                 | 271 ms: 1.08x faster                                               |
| mdp                     | 2.63 sec                                               | 2.45 sec: 1.07x faster                                             |
| chaos                   | 68.7 ms                                                | 64.1 ms: 1.07x faster                                              |
| pickle_pure_python      | 308 us                                                 | 288 us: 1.07x faster                                               |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                               |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                              |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                               |
| hexiom                  | 6.34 ms                                                | 5.95 ms: 1.07x faster                                              |
| float                   | 76.8 ms                                                | 72.1 ms: 1.07x faster                                              |
| html5lib                | 64.8 ms                                                | 60.9 ms: 1.06x faster                                              |
| nqueens                 | 83.8 ms                                                | 78.8 ms: 1.06x faster                                              |
| crypto_pyaes            | 75.7 ms                                                | 71.3 ms: 1.06x faster                                              |
| logging_silent          | 98.0 ns                                                | 92.3 ns: 1.06x faster                                              |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                              |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                              |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                              |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                               |
| nbody                   | 90.0 ms                                                | 86.0 ms: 1.05x faster                                              |
| scimark_monte_carlo     | 68.0 ms                                                | 65.0 ms: 1.05x faster                                              |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                             |
| unpack_sequence         | 44.5 ns                                                | 42.6 ns: 1.04x faster                                              |
| fannkuch                | 384 ms                                                 | 369 ms: 1.04x faster                                               |
| regex_effbot            | 3.46 ms                                                | 3.32 ms: 1.04x faster                                              |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                               |
| regex_v8                | 22.2 ms                                                | 21.4 ms: 1.04x faster                                              |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                               |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                               |
| logging_simple          | 6.02 us                                                | 5.79 us: 1.04x faster                                              |
| bench_thread_pool       | 817 us                                                 | 786 us: 1.04x faster                                               |
| pyflate                 | 419 ms                                                 | 403 ms: 1.04x faster                                               |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                               |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 680 ms: 1.04x faster                                               |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                              |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                              |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                              |
| djangocms               | 32.5 us                                                | 31.6 us: 1.03x faster                                              |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                              |
| tornado_http            | 96.5 ms                                                | 94.0 ms: 1.03x faster                                              |
| spectral_norm           | 98.1 ms                                                | 95.9 ms: 1.02x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                               |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                              |
| coverage                | 99.3 ms                                                | 97.3 ms: 1.02x faster                                              |
| mako                    | 9.83 ms                                                | 9.65 ms: 1.02x faster                                              |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                              |
| docutils                | 2.60 sec                                               | 2.56 sec: 1.02x faster                                             |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                              |
| pickle_list             | 4.14 us                                                | 4.09 us: 1.01x faster                                              |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.01x faster                                               |
| dulwich_log             | 64.0 ms                                                | 63.1 ms: 1.01x faster                                              |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                               |
| thrift                  | 760 us                                                 | 765 us: 1.01x slower                                               |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 752 ms: 1.02x slower                                               |
| meteor_contest          | 104 ms                                                 | 107 ms: 1.03x slower                                               |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                              |
| xml_etree_process       | 53.7 ms                                                | 55.6 ms: 1.04x slower                                              |
| gc_traversal            | 3.82 ms                                                | 3.96 ms: 1.04x slower                                              |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                              |
| xml_etree_iterparse     | 104 ms                                                 | 108 ms: 1.04x slower                                               |
| generators              | 73.5 ms                                                | 76.5 ms: 1.04x slower                                              |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                              |
| xml_etree_generate      | 75.9 ms                                                | 81.3 ms: 1.07x slower                                              |
| python_startup_no_site  | 6.04 ms                                                | 6.51 ms: 1.08x slower                                              |
| async_generators        | 356 ms                                                 | 423 ms: 1.19x slower                                               |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (9): unpickle, async_tree_none, telco, sqlalchemy_imperative, chameleon, async_tree_io, bench_mp_pool, django_template, async_tree_memoization
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
