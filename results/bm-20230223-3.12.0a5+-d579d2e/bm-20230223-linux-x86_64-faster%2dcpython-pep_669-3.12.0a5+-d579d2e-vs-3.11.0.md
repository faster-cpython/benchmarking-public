
# Results vs. 3.11.0

- fork: faster-cpython
- ref: pep_669
- machine: linux-x86_64
- commit hash: d579d2e
- commit date: 2023-02-23
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                |
| chameleon      | 6.38 ms                                                | 6.26 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 59.8 ms: 1.08x faster                                               |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.4 ms: 1.05x faster                                               |
| pidigits       | 197 ms                                                 | 192 ms: 1.02x faster                                                |
| nbody          | 90.0 ms                                                | 92.2 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                               |
| regex_dna      | 203 ms                                                 | 200 ms: 1.01x faster                                                |
| regex_effbot   | 3.46 ms                                                | 3.63 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.32x faster                                               |
| unpickle_pure_python | 227 us                                                 | 194 us: 1.17x faster                                                |
| pickle_pure_python   | 308 us                                                 | 277 us: 1.11x faster                                                |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 99.7 ms: 1.04x faster                                               |
| xml_etree_process    | 53.7 ms                                                | 54.4 ms: 1.01x slower                                               |
| pickle_dict          | 31.2 us                                                | 31.7 us: 1.02x slower                                               |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                               |
| pickle_list          | 4.14 us                                                | 4.27 us: 1.03x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 79.4 ms: 1.05x slower                                               |
| unpickle             | 13.3 us                                                | 13.9 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.06 ms: 1.06x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.58 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 45.9 ms: 1.12x faster                                               |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                               |
| mako            | 9.83 ms                                                | 9.75 ms: 1.01x faster                                               |
| django_template | 32.3 ms                                                | 32.8 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.6 ms: 2.33x faster                                               |
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.77x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.32x faster                                               |
| mypy2                   | 420 ms                                                 | 327 ms: 1.28x faster                                                |
| coroutines              | 26.2 ms                                                | 22.0 ms: 1.19x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 194 us: 1.17x faster                                                |
| deltablue               | 3.66 ms                                                | 3.14 ms: 1.17x faster                                               |
| genshi_xml              | 51.4 ms                                                | 45.9 ms: 1.12x faster                                               |
| pickle_pure_python      | 308 us                                                 | 277 us: 1.11x faster                                                |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                                |
| richards                | 46.1 ms                                                | 41.6 ms: 1.11x faster                                               |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                               |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                              |
| deepcopy_memo           | 35.8 us                                                | 33.1 us: 1.08x faster                                               |
| html5lib                | 64.8 ms                                                | 59.8 ms: 1.08x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| fannkuch                | 384 ms                                                 | 357 ms: 1.08x faster                                                |
| go                      | 140 ms                                                 | 130 ms: 1.08x faster                                                |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                                |
| nqueens                 | 83.8 ms                                                | 78.4 ms: 1.07x faster                                               |
| logging_silent          | 98.0 ns                                                | 91.7 ns: 1.07x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 662 ms: 1.07x faster                                                |
| json                    | 4.87 ms                                                | 4.58 ms: 1.06x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                              |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| scimark_monte_carlo     | 68.0 ms                                                | 64.2 ms: 1.06x faster                                               |
| deepcopy                | 341 us                                                 | 323 us: 1.06x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 102 ms: 1.06x faster                                                |
| hexiom                  | 6.34 ms                                                | 6.00 ms: 1.06x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.34 ms: 1.06x faster                                               |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.06x faster                                                |
| sqlglot_optimize        | 52.7 ms                                                | 50.1 ms: 1.05x faster                                               |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                               |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                               |
| float                   | 76.8 ms                                                | 73.4 ms: 1.05x faster                                               |
| crypto_pyaes            | 75.7 ms                                                | 72.4 ms: 1.05x faster                                               |
| pyflate                 | 419 ms                                                 | 401 ms: 1.05x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 99.7 ms: 1.04x faster                                               |
| bench_thread_pool       | 817 us                                                 | 782 us: 1.04x faster                                                |
| sympy_str               | 291 ms                                                 | 279 ms: 1.04x faster                                                |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                               |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                |
| dulwich_log             | 64.0 ms                                                | 61.6 ms: 1.04x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                               |
| spectral_norm           | 98.1 ms                                                | 94.6 ms: 1.04x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| chaos                   | 68.7 ms                                                | 66.2 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 43.1 ns: 1.03x faster                                               |
| tornado_http            | 96.5 ms                                                | 93.8 ms: 1.03x faster                                               |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.03x faster                                               |
| pidigits                | 197 ms                                                 | 192 ms: 1.02x faster                                                |
| coverage                | 99.3 ms                                                | 96.9 ms: 1.02x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.02x faster                                               |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                               |
| chameleon               | 6.38 ms                                                | 6.26 ms: 1.02x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| regex_dna               | 203 ms                                                 | 200 ms: 1.01x faster                                                |
| telco                   | 6.43 ms                                                | 6.35 ms: 1.01x faster                                               |
| mdp                     | 2.63 sec                                               | 2.60 sec: 1.01x faster                                              |
| mako                    | 9.83 ms                                                | 9.75 ms: 1.01x faster                                               |
| sympy_sum               | 166 ms                                                 | 165 ms: 1.01x faster                                                |
| gc_traversal            | 3.82 ms                                                | 3.83 ms: 1.00x slower                                               |
| xml_etree_process       | 53.7 ms                                                | 54.4 ms: 1.01x slower                                               |
| django_template         | 32.3 ms                                                | 32.8 ms: 1.02x slower                                               |
| pickle_dict             | 31.2 us                                                | 31.7 us: 1.02x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.68 ms: 1.02x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.39 ms: 1.02x slower                                               |
| nbody                   | 90.0 ms                                                | 92.2 ms: 1.02x slower                                               |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                               |
| pickle_list             | 4.14 us                                                | 4.27 us: 1.03x slower                                               |
| async_tree_memoization  | 624 ms                                                 | 646 ms: 1.04x slower                                                |
| xml_etree_generate      | 75.9 ms                                                | 79.4 ms: 1.05x slower                                               |
| unpickle                | 13.3 us                                                | 13.9 us: 1.05x slower                                               |
| regex_effbot            | 3.46 ms                                                | 3.63 ms: 1.05x slower                                               |
| python_startup          | 8.58 ms                                                | 9.06 ms: 1.06x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.58 ms: 1.09x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.73 us: 1.10x slower                                               |
| async_generators        | 356 ms                                                 | 430 ms: 1.21x slower                                                |
| dask                    | 365 ms                                                 | 490 ms: 1.34x slower                                                |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (9): djangocms, thrift, logging_format, create_gc_cycles, unpickle_list, async_tree_none, bench_mp_pool, async_tree_io, async_tree_cpu_io_mixed
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
