
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 4b64c3e
- commit date: 2023-02-08
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.03x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                        |
| tornado_http   | 96.5 ms                                                | 94.8 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.0 ms: 1.05x faster                                                        |
| pidigits       | 197 ms                                                 | 192 ms: 1.03x faster                                                         |
| nbody          | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                         |
| regex_v8       | 22.2 ms                                                | 22.0 ms: 1.01x faster                                                        |
| regex_effbot   | 3.46 ms                                                | 3.52 ms: 1.02x slower                                                        |
| regex_dna      | 203 ms                                                 | 218 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.33 ms: 1.32x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                         |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 294 us: 1.05x faster                                                         |
| pickle_dict          | 31.2 us                                                | 30.4 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                        |
| xml_etree_process    | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 80.5 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (3): pickle_list, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.86 ms: 1.03x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.42 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                        |
| genshi_text    | 21.5 ms                                                | 20.8 ms: 1.03x faster                                                        |
| mako           | 9.83 ms                                                | 9.90 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 505 ms: 1.75x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.33 ms: 1.32x faster                                                        |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                         |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.14x faster                                                        |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                         |
| nqueens                 | 83.8 ms                                                | 76.2 ms: 1.10x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                        |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.08x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                         |
| richards                | 46.1 ms                                                | 42.8 ms: 1.08x faster                                                        |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.27 ms: 1.07x faster                                                        |
| sympy_str               | 291 ms                                                 | 271 ms: 1.07x faster                                                         |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                        |
| fannkuch                | 384 ms                                                 | 361 ms: 1.07x faster                                                         |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                                        |
| html5lib                | 64.8 ms                                                | 61.0 ms: 1.06x faster                                                        |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                        |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                                         |
| float                   | 76.8 ms                                                | 73.0 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                         |
| spectral_norm           | 98.1 ms                                                | 93.4 ms: 1.05x faster                                                        |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                         |
| pickle_pure_python      | 308 us                                                 | 294 us: 1.05x faster                                                         |
| gc_traversal            | 3.82 ms                                                | 3.65 ms: 1.05x faster                                                        |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                                         |
| json                    | 4.87 ms                                                | 4.66 ms: 1.04x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                        |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                        |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.03x faster                                                        |
| chaos                   | 68.7 ms                                                | 66.4 ms: 1.03x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.02 ms: 1.03x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 791 us: 1.03x faster                                                         |
| pyflate                 | 419 ms                                                 | 406 ms: 1.03x faster                                                         |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                                         |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                         |
| crypto_pyaes            | 75.7 ms                                                | 73.6 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                                         |
| scimark_monte_carlo     | 68.0 ms                                                | 66.1 ms: 1.03x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                                       |
| pickle_dict             | 31.2 us                                                | 30.4 us: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.03x faster                                                       |
| pidigits                | 197 ms                                                 | 192 ms: 1.03x faster                                                         |
| logging_silent          | 98.0 ns                                                | 95.9 ns: 1.02x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.02x faster                                                        |
| raytrace                | 291 ms                                                 | 286 ms: 1.02x faster                                                         |
| tornado_http            | 96.5 ms                                                | 94.8 ms: 1.02x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 51.8 ms: 1.02x faster                                                        |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                                         |
| logging_simple          | 6.02 us                                                | 5.95 us: 1.01x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| regex_v8                | 22.2 ms                                                | 22.0 ms: 1.01x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 63.6 ms: 1.01x faster                                                        |
| mako                    | 9.83 ms                                                | 9.90 ms: 1.01x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                       |
| coverage                | 99.3 ms                                                | 101 ms: 1.02x slower                                                         |
| regex_effbot            | 3.46 ms                                                | 3.52 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 749 ms: 1.02x slower                                                         |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                        |
| sqlalchemy_imperative   | 18.1 ms                                                | 18.4 ms: 1.02x slower                                                        |
| mdp                     | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                       |
| xml_etree_process       | 53.7 ms                                                | 55.3 ms: 1.03x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.86 ms: 1.03x slower                                                        |
| async_tree_memoization  | 624 ms                                                 | 645 ms: 1.03x slower                                                         |
| nbody                   | 90.0 ms                                                | 93.1 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                        |
| generators              | 73.5 ms                                                | 76.9 ms: 1.05x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.05x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 80.5 ms: 1.06x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.06x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.42 ms: 1.06x slower                                                        |
| regex_dna               | 203 ms                                                 | 218 ms: 1.07x slower                                                         |
| async_generators        | 356 ms                                                 | 435 ms: 1.22x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (16): sqlalchemy_declarative, unpack_sequence, async_tree_none, chameleon, pathlib, djangocms, pickle_list, telco, scimark_lu, sqlglot_normalize, thrift, unpickle_list, bench_mp_pool, logging_format, django_template, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
