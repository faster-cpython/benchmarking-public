
# Results vs. 3.11.0

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 1a4b9a9
- commit date: 2023-02-08
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                               |
| chameleon      | 6.41 ms                                                | 6.36 ms: 1.01x faster                                              |
| docutils       | 2.60 sec                                               | 2.56 sec: 1.02x faster                                             |
| html5lib       | 63.2 ms                                                | 60.9 ms: 1.04x faster                                              |
| tornado_http   | 96.6 ms                                                | 94.0 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 95.0 ms                                                | 86.0 ms: 1.11x faster                                              |
| float          | 76.3 ms                                                | 72.1 ms: 1.06x faster                                              |
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                               |
| regex_v8       | 22.3 ms                                                | 21.4 ms: 1.04x faster                                              |
| regex_effbot   | 3.36 ms                                                | 3.32 ms: 1.01x faster                                              |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.34 ms: 1.36x faster                                              |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                               |
| json_loads           | 26.2 us                                                | 23.7 us: 1.11x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                               |
| pickle_pure_python   | 304 us                                                 | 288 us: 1.05x faster                                               |
| pickle_dict          | 31.4 us                                                | 30.6 us: 1.03x faster                                              |
| pickle_list          | 4.17 us                                                | 4.09 us: 1.02x faster                                              |
| unpickle_list        | 4.95 us                                                | 5.04 us: 1.02x slower                                              |
| xml_etree_process    | 53.8 ms                                                | 55.6 ms: 1.03x slower                                              |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                              |
| xml_etree_iterparse  | 103 ms                                                 | 108 ms: 1.06x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 81.3 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.97 ms: 1.07x slower                                              |
| python_startup_no_site | 5.96 ms                                                | 6.51 ms: 1.09x slower                                              |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 46.4 ms: 1.12x faster                                              |
| genshi_text    | 22.1 ms                                                | 20.7 ms: 1.07x faster                                              |
| mako           | 9.85 ms                                                | 9.65 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.34 ms: 1.36x faster                                              |
| deltablue               | 3.64 ms                                                | 3.18 ms: 1.15x faster                                              |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.90 ms: 1.13x faster                                              |
| genshi_xml              | 52.1 ms                                                | 46.4 ms: 1.12x faster                                              |
| nbody                   | 95.0 ms                                                | 86.0 ms: 1.11x faster                                              |
| json_loads              | 26.2 us                                                | 23.7 us: 1.11x faster                                              |
| scimark_fft             | 329 ms                                                 | 298 ms: 1.10x faster                                               |
| richards                | 46.2 ms                                                | 42.2 ms: 1.09x faster                                              |
| nqueens                 | 85.0 ms                                                | 78.8 ms: 1.08x faster                                              |
| deepcopy_memo           | 36.4 us                                                | 33.9 us: 1.08x faster                                              |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                             |
| chaos                   | 68.6 ms                                                | 64.1 ms: 1.07x faster                                              |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                               |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.07x faster                                             |
| hexiom                  | 6.35 ms                                                | 5.95 ms: 1.07x faster                                              |
| json                    | 4.95 ms                                                | 4.64 ms: 1.07x faster                                              |
| logging_silent          | 98.5 ns                                                | 92.3 ns: 1.07x faster                                              |
| genshi_text             | 22.1 ms                                                | 20.7 ms: 1.07x faster                                              |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.06x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                               |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                               |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                               |
| float                   | 76.3 ms                                                | 72.1 ms: 1.06x faster                                              |
| pickle_pure_python      | 304 us                                                 | 288 us: 1.05x faster                                               |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                               |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                              |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                               |
| scimark_monte_carlo     | 68.3 ms                                                | 65.0 ms: 1.05x faster                                              |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                               |
| deepcopy                | 344 us                                                 | 328 us: 1.05x faster                                               |
| logging_simple          | 6.06 us                                                | 5.79 us: 1.05x faster                                              |
| logging_format          | 6.62 us                                                | 6.34 us: 1.04x faster                                              |
| regex_v8                | 22.3 ms                                                | 21.4 ms: 1.04x faster                                              |
| spectral_norm           | 99.9 ms                                                | 95.9 ms: 1.04x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                              |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                              |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                              |
| html5lib                | 63.2 ms                                                | 60.9 ms: 1.04x faster                                              |
| crypto_pyaes            | 73.9 ms                                                | 71.3 ms: 1.04x faster                                              |
| pyflate                 | 417 ms                                                 | 403 ms: 1.04x faster                                               |
| telco                   | 6.62 ms                                                | 6.40 ms: 1.03x faster                                              |
| raytrace                | 290 ms                                                 | 281 ms: 1.03x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                             |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                               |
| coverage                | 101 ms                                                 | 97.3 ms: 1.03x faster                                              |
| bench_thread_pool       | 810 us                                                 | 786 us: 1.03x faster                                               |
| tornado_http            | 96.6 ms                                                | 94.0 ms: 1.03x faster                                              |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                               |
| pickle_dict             | 31.4 us                                                | 30.6 us: 1.03x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                               |
| pickle_list             | 4.17 us                                                | 4.09 us: 1.02x faster                                              |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                              |
| mako                    | 9.85 ms                                                | 9.65 ms: 1.02x faster                                              |
| unpack_sequence         | 43.4 ns                                                | 42.6 ns: 1.02x faster                                              |
| deepcopy_reduce         | 2.97 us                                                | 2.92 us: 1.02x faster                                              |
| pprint_safe_repr        | 691 ms                                                 | 680 ms: 1.02x faster                                               |
| docutils                | 2.60 sec                                               | 2.56 sec: 1.02x faster                                             |
| sqlalchemy_declarative  | 139 ms                                                 | 137 ms: 1.01x faster                                               |
| dulwich_log             | 63.9 ms                                                | 63.1 ms: 1.01x faster                                              |
| async_tree_none         | 529 ms                                                 | 523 ms: 1.01x faster                                               |
| regex_effbot            | 3.36 ms                                                | 3.32 ms: 1.01x faster                                              |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                               |
| chameleon               | 6.41 ms                                                | 6.36 ms: 1.01x faster                                              |
| thrift                  | 752 us                                                 | 765 us: 1.02x slower                                               |
| unpickle_list           | 4.95 us                                                | 5.04 us: 1.02x slower                                              |
| meteor_contest          | 105 ms                                                 | 107 ms: 1.03x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                              |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                              |
| xml_etree_process       | 53.8 ms                                                | 55.6 ms: 1.03x slower                                              |
| sqlglot_transpile       | 1.66 ms                                                | 1.72 ms: 1.03x slower                                              |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                              |
| xml_etree_iterparse     | 103 ms                                                 | 108 ms: 1.06x slower                                               |
| generators              | 72.2 ms                                                | 76.5 ms: 1.06x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 81.3 ms: 1.07x slower                                              |
| python_startup          | 8.36 ms                                                | 8.97 ms: 1.07x slower                                              |
| python_startup_no_site  | 5.96 ms                                                | 6.51 ms: 1.09x slower                                              |
| async_generators        | 359 ms                                                 | 423 ms: 1.18x slower                                               |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (7): unpickle, async_tree_io, django_template, sqlalchemy_imperative, bench_mp_pool, async_tree_cpu_io_mixed, async_tree_memoization
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230208-3.12.0a5+-1a4b9a9/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
