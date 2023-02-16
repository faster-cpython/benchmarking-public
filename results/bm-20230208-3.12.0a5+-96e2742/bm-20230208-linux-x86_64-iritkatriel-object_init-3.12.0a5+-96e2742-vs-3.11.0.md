
# Results vs. 3.11.0

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 96e2742
- commit date: 2023-02-08
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                               |
| chameleon      | 6.38 ms                                                | 6.48 ms: 1.02x slower                                              |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                             |
| html5lib       | 64.8 ms                                                | 60.8 ms: 1.07x faster                                              |
| tornado_http   | 96.5 ms                                                | 94.1 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.8 ms: 1.07x faster                                              |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                               |
| nbody          | 90.0 ms                                                | 86.6 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                               |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.02x faster                                              |
| regex_effbot   | 3.46 ms                                                | 3.40 ms: 1.02x faster                                              |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                              |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                               |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                               |
| pickle_pure_python   | 308 us                                                 | 289 us: 1.07x faster                                               |
| pickle_list          | 4.14 us                                                | 4.03 us: 1.03x faster                                              |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.00x faster                                              |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                               |
| xml_etree_process    | 53.7 ms                                                | 55.4 ms: 1.03x slower                                              |
| xml_etree_generate   | 75.9 ms                                                | 80.0 ms: 1.05x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.90 ms: 1.04x slower                                              |
| python_startup_no_site | 6.04 ms                                                | 6.45 ms: 1.07x slower                                              |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.3 ms: 1.11x faster                                              |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                              |
| mako            | 9.83 ms                                                | 9.64 ms: 1.02x faster                                              |
| django_template | 32.3 ms                                                | 32.5 ms: 1.00x slower                                              |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 493 ms: 1.79x faster                                               |
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                              |
| mypy2                   | 420 ms                                                 | 329 ms: 1.28x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.91 ms: 1.17x faster                                              |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                              |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                               |
| genshi_xml              | 51.4 ms                                                | 46.3 ms: 1.11x faster                                              |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                              |
| scimark_fft             | 325 ms                                                 | 298 ms: 1.09x faster                                               |
| richards                | 46.1 ms                                                | 42.6 ms: 1.08x faster                                              |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                             |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                               |
| sympy_str               | 291 ms                                                 | 271 ms: 1.08x faster                                               |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                               |
| float                   | 76.8 ms                                                | 71.8 ms: 1.07x faster                                              |
| chaos                   | 68.7 ms                                                | 64.3 ms: 1.07x faster                                              |
| pickle_pure_python      | 308 us                                                 | 289 us: 1.07x faster                                               |
| json                    | 4.87 ms                                                | 4.56 ms: 1.07x faster                                              |
| html5lib                | 64.8 ms                                                | 60.8 ms: 1.07x faster                                              |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                               |
| nqueens                 | 83.8 ms                                                | 78.9 ms: 1.06x faster                                              |
| hexiom                  | 6.34 ms                                                | 6.00 ms: 1.06x faster                                              |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.05x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                             |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                              |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                              |
| pprint_safe_repr        | 706 ms                                                 | 674 ms: 1.05x faster                                               |
| gc_traversal            | 3.82 ms                                                | 3.65 ms: 1.05x faster                                              |
| logging_silent          | 98.0 ns                                                | 93.6 ns: 1.05x faster                                              |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                               |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                              |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.04x faster                                              |
| deepcopy_memo           | 35.8 us                                                | 34.3 us: 1.04x faster                                              |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.04x faster                                              |
| bench_thread_pool       | 817 us                                                 | 784 us: 1.04x faster                                               |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                               |
| spectral_norm           | 98.1 ms                                                | 94.3 ms: 1.04x faster                                              |
| nbody                   | 90.0 ms                                                | 86.6 ms: 1.04x faster                                              |
| coroutines              | 26.2 ms                                                | 25.2 ms: 1.04x faster                                              |
| pyflate                 | 419 ms                                                 | 403 ms: 1.04x faster                                               |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                               |
| crypto_pyaes            | 75.7 ms                                                | 73.0 ms: 1.04x faster                                              |
| raytrace                | 291 ms                                                 | 282 ms: 1.04x faster                                               |
| scimark_monte_carlo     | 68.0 ms                                                | 65.8 ms: 1.03x faster                                              |
| logging_format          | 6.48 us                                                | 6.27 us: 1.03x faster                                              |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                              |
| pathlib                 | 18.1 ms                                                | 17.5 ms: 1.03x faster                                              |
| pickle_list             | 4.14 us                                                | 4.03 us: 1.03x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                               |
| tornado_http            | 96.5 ms                                                | 94.1 ms: 1.03x faster                                              |
| coverage                | 99.3 ms                                                | 96.9 ms: 1.02x faster                                              |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.02x faster                                              |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                             |
| mako                    | 9.83 ms                                                | 9.64 ms: 1.02x faster                                              |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                              |
| regex_effbot            | 3.46 ms                                                | 3.40 ms: 1.02x faster                                              |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                               |
| fannkuch                | 384 ms                                                 | 382 ms: 1.01x faster                                               |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.00x faster                                              |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.00x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                             |
| mdp                     | 2.63 sec                                               | 2.66 sec: 1.01x slower                                             |
| chameleon               | 6.38 ms                                                | 6.48 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 751 ms: 1.02x slower                                               |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.55 us: 1.03x slower                                              |
| xml_etree_process       | 53.7 ms                                                | 55.4 ms: 1.03x slower                                              |
| meteor_contest          | 104 ms                                                 | 108 ms: 1.04x slower                                               |
| python_startup          | 8.58 ms                                                | 8.90 ms: 1.04x slower                                              |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                              |
| async_tree_memoization  | 624 ms                                                 | 652 ms: 1.04x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 80.0 ms: 1.05x slower                                              |
| generators              | 73.5 ms                                                | 78.2 ms: 1.06x slower                                              |
| python_startup_no_site  | 6.04 ms                                                | 6.45 ms: 1.07x slower                                              |
| async_generators        | 356 ms                                                 | 431 ms: 1.21x slower                                               |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (10): unpickle, async_tree_none, thrift, sqlalchemy_declarative, unpickle_list, sqlalchemy_imperative, bench_mp_pool, unpack_sequence, djangocms, telco
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
