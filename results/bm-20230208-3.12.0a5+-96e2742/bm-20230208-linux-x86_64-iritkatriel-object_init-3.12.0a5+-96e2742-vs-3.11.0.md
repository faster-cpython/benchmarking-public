
# Results vs. 3.11.0

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 96e2742
- commit date: 2023-02-08
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.02x faster                                               |
| chameleon      | 6.41 ms                                                | 6.48 ms: 1.01x slower                                              |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                             |
| html5lib       | 63.2 ms                                                | 60.8 ms: 1.04x faster                                              |
| tornado_http   | 96.6 ms                                                | 94.1 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 95.0 ms                                                | 86.6 ms: 1.10x faster                                              |
| float          | 76.3 ms                                                | 71.8 ms: 1.06x faster                                              |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                               |
| regex_v8       | 22.3 ms                                                | 21.7 ms: 1.03x faster                                              |
| regex_effbot   | 3.36 ms                                                | 3.40 ms: 1.01x slower                                              |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.44 ms: 1.34x faster                                              |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                               |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                               |
| pickle_pure_python   | 304 us                                                 | 289 us: 1.05x faster                                               |
| pickle_list          | 4.17 us                                                | 4.03 us: 1.04x faster                                              |
| pickle_dict          | 31.4 us                                                | 31.0 us: 1.01x faster                                              |
| xml_etree_process    | 53.8 ms                                                | 55.4 ms: 1.03x slower                                              |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                              |
| xml_etree_iterparse  | 103 ms                                                 | 107 ms: 1.04x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 80.0 ms: 1.05x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.90 ms: 1.06x slower                                              |
| python_startup_no_site | 5.96 ms                                                | 6.45 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 46.3 ms: 1.12x faster                                              |
| genshi_text    | 22.1 ms                                                | 20.5 ms: 1.08x faster                                              |
| mako           | 9.85 ms                                                | 9.64 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.44 ms: 1.34x faster                                              |
| deltablue               | 3.64 ms                                                | 3.19 ms: 1.14x faster                                              |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.91 ms: 1.13x faster                                              |
| genshi_xml              | 52.1 ms                                                | 46.3 ms: 1.12x faster                                              |
| scimark_fft             | 329 ms                                                 | 298 ms: 1.10x faster                                               |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                              |
| nbody                   | 95.0 ms                                                | 86.6 ms: 1.10x faster                                              |
| json                    | 4.95 ms                                                | 4.56 ms: 1.08x faster                                              |
| richards                | 46.2 ms                                                | 42.6 ms: 1.08x faster                                              |
| nqueens                 | 85.0 ms                                                | 78.9 ms: 1.08x faster                                              |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                              |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                               |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.07x faster                                             |
| chaos                   | 68.6 ms                                                | 64.3 ms: 1.07x faster                                              |
| float                   | 76.3 ms                                                | 71.8 ms: 1.06x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                               |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                               |
| deepcopy_memo           | 36.4 us                                                | 34.3 us: 1.06x faster                                              |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                               |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                               |
| spectral_norm           | 99.9 ms                                                | 94.3 ms: 1.06x faster                                              |
| hexiom                  | 6.35 ms                                                | 6.00 ms: 1.06x faster                                              |
| logging_simple          | 6.06 us                                                | 5.74 us: 1.06x faster                                              |
| logging_format          | 6.62 us                                                | 6.27 us: 1.06x faster                                              |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                               |
| pickle_pure_python      | 304 us                                                 | 289 us: 1.05x faster                                               |
| logging_silent          | 98.5 ns                                                | 93.6 ns: 1.05x faster                                              |
| deepcopy                | 344 us                                                 | 327 us: 1.05x faster                                               |
| sympy_integrate         | 20.9 ms                                                | 19.9 ms: 1.05x faster                                              |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                             |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                              |
| sympy_expand            | 472 ms                                                 | 455 ms: 1.04x faster                                               |
| html5lib                | 63.2 ms                                                | 60.8 ms: 1.04x faster                                              |
| scimark_monte_carlo     | 68.3 ms                                                | 65.8 ms: 1.04x faster                                              |
| coverage                | 101 ms                                                 | 96.9 ms: 1.04x faster                                              |
| sqlglot_optimize        | 53.0 ms                                                | 51.1 ms: 1.04x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                              |
| pickle_list             | 4.17 us                                                | 4.03 us: 1.04x faster                                              |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                              |
| coroutines              | 26.1 ms                                                | 25.2 ms: 1.04x faster                                              |
| pyflate                 | 417 ms                                                 | 403 ms: 1.03x faster                                               |
| bench_thread_pool       | 810 us                                                 | 784 us: 1.03x faster                                               |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                               |
| tornado_http            | 96.6 ms                                                | 94.1 ms: 1.03x faster                                              |
| deepcopy_reduce         | 2.97 us                                                | 2.89 us: 1.03x faster                                              |
| regex_v8                | 22.3 ms                                                | 21.7 ms: 1.03x faster                                              |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.03x faster                                               |
| 2to3                    | 257 ms                                                 | 251 ms: 1.02x faster                                               |
| telco                   | 6.62 ms                                                | 6.47 ms: 1.02x faster                                              |
| mako                    | 9.85 ms                                                | 9.64 ms: 1.02x faster                                              |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                             |
| fannkuch                | 388 ms                                                 | 382 ms: 1.02x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.9 ms: 1.02x faster                                              |
| pickle_dict             | 31.4 us                                                | 31.0 us: 1.01x faster                                              |
| crypto_pyaes            | 73.9 ms                                                | 73.0 ms: 1.01x faster                                              |
| async_tree_none         | 529 ms                                                 | 523 ms: 1.01x faster                                               |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                             |
| chameleon               | 6.41 ms                                                | 6.48 ms: 1.01x slower                                              |
| regex_effbot            | 3.36 ms                                                | 3.40 ms: 1.01x slower                                              |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                             |
| sqlite_synth            | 2.49 us                                                | 2.55 us: 1.03x slower                                              |
| unpack_sequence         | 43.4 ns                                                | 44.6 ns: 1.03x slower                                              |
| xml_etree_process       | 53.8 ms                                                | 55.4 ms: 1.03x slower                                              |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                              |
| meteor_contest          | 105 ms                                                 | 108 ms: 1.03x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.72 ms: 1.03x slower                                              |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                              |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| xml_etree_iterparse     | 103 ms                                                 | 107 ms: 1.04x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 652 ms: 1.04x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 80.0 ms: 1.05x slower                                              |
| python_startup          | 8.36 ms                                                | 8.90 ms: 1.06x slower                                              |
| python_startup_no_site  | 5.96 ms                                                | 6.45 ms: 1.08x slower                                              |
| generators              | 72.2 ms                                                | 78.2 ms: 1.08x slower                                              |
| async_generators        | 359 ms                                                 | 431 ms: 1.20x slower                                               |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (9): unpickle, scimark_lu, sqlalchemy_declarative, async_tree_cpu_io_mixed, bench_mp_pool, django_template, sqlalchemy_imperative, unpickle_list, thrift
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230208-3.12.0a5+-96e2742/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
