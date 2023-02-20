
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 4c82d9e
- commit date: 2023-02-20
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| chameleon      | 6.38 ms                                                | 6.25 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                              |
| html5lib       | 64.8 ms                                                | 61.7 ms: 1.05x faster                                               |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.2 ms: 1.06x faster                                               |
| pidigits       | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| nbody          | 90.0 ms                                                | 94.6 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                               |
| regex_dna      | 203 ms                                                 | 199 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                               |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                |
| json_loads           | 26.1 us                                                | 23.8 us: 1.09x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| pickle_pure_python   | 308 us                                                 | 290 us: 1.06x faster                                                |
| pickle_dict          | 31.2 us                                                | 29.7 us: 1.05x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.80 us: 1.04x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pickle_list          | 4.14 us                                                | 4.08 us: 1.01x faster                                               |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                               |
| xml_etree_process    | 53.7 ms                                                | 57.2 ms: 1.07x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 82.2 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.95 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.50 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.6 ms: 1.08x faster                                               |
| genshi_text     | 21.5 ms                                                | 20.7 ms: 1.04x faster                                               |
| mako            | 9.83 ms                                                | 9.51 ms: 1.03x faster                                               |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                               |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.96 ms: 1.16x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                               |
| richards                | 46.1 ms                                                | 42.0 ms: 1.10x faster                                               |
| json_loads              | 26.1 us                                                | 23.8 us: 1.09x faster                                               |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| genshi_xml              | 51.4 ms                                                | 47.6 ms: 1.08x faster                                               |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                              |
| scimark_fft             | 325 ms                                                 | 303 ms: 1.08x faster                                                |
| nqueens                 | 83.8 ms                                                | 78.2 ms: 1.07x faster                                               |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| logging_silent          | 98.0 ns                                                | 91.6 ns: 1.07x faster                                               |
| pickle_pure_python      | 308 us                                                 | 290 us: 1.06x faster                                                |
| float                   | 76.8 ms                                                | 72.2 ms: 1.06x faster                                               |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                               |
| chaos                   | 68.7 ms                                                | 65.0 ms: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| aiohttp                 | 1.05 ms                                                | 997 us: 1.05x faster                                                |
| pyflate                 | 419 ms                                                 | 398 ms: 1.05x faster                                                |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                               |
| sympy_sum               | 166 ms                                                 | 158 ms: 1.05x faster                                                |
| html5lib                | 64.8 ms                                                | 61.7 ms: 1.05x faster                                               |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                               |
| pickle_dict             | 31.2 us                                                | 29.7 us: 1.05x faster                                               |
| logging_simple          | 6.02 us                                                | 5.75 us: 1.05x faster                                               |
| spectral_norm           | 98.1 ms                                                | 93.8 ms: 1.05x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 42.5 ns: 1.05x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                               |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                                |
| mdp                     | 2.63 sec                                               | 2.52 sec: 1.04x faster                                              |
| scimark_monte_carlo     | 68.0 ms                                                | 65.3 ms: 1.04x faster                                               |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.80 us: 1.04x faster                                               |
| fannkuch                | 384 ms                                                 | 370 ms: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                                |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                                |
| go                      | 140 ms                                                 | 136 ms: 1.04x faster                                                |
| pidigits                | 197 ms                                                 | 191 ms: 1.03x faster                                                |
| mako                    | 9.83 ms                                                | 9.51 ms: 1.03x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                               |
| logging_format          | 6.48 us                                                | 6.27 us: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                               |
| dulwich_log             | 64.0 ms                                                | 62.0 ms: 1.03x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 685 ms: 1.03x faster                                                |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                               |
| tornado_http            | 96.5 ms                                                | 93.8 ms: 1.03x faster                                               |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                              |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| regex_dna               | 203 ms                                                 | 199 ms: 1.02x faster                                                |
| sqlglot_optimize        | 52.7 ms                                                | 51.7 ms: 1.02x faster                                               |
| chameleon               | 6.38 ms                                                | 6.25 ms: 1.02x faster                                               |
| coroutines              | 26.2 ms                                                | 25.7 ms: 1.02x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                |
| pickle_list             | 4.14 us                                                | 4.08 us: 1.01x faster                                               |
| coverage                | 99.3 ms                                                | 97.9 ms: 1.01x faster                                               |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.9 ms: 1.01x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| meteor_contest          | 104 ms                                                 | 105 ms: 1.01x slower                                                |
| crypto_pyaes            | 75.7 ms                                                | 76.4 ms: 1.01x slower                                               |
| async_tree_none         | 526 ms                                                 | 532 ms: 1.01x slower                                                |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                              |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                               |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                               |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 759 ms: 1.03x slower                                                |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                               |
| python_startup          | 8.58 ms                                                | 8.95 ms: 1.04x slower                                               |
| nbody                   | 90.0 ms                                                | 94.6 ms: 1.05x slower                                               |
| generators              | 73.5 ms                                                | 77.3 ms: 1.05x slower                                               |
| xml_etree_process       | 53.7 ms                                                | 57.2 ms: 1.07x slower                                               |
| async_tree_memoization  | 624 ms                                                 | 666 ms: 1.07x slower                                                |
| python_startup_no_site  | 6.04 ms                                                | 6.50 ms: 1.08x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 82.2 ms: 1.08x slower                                               |
| gc_traversal            | 3.82 ms                                                | 4.29 ms: 1.12x slower                                               |
| async_generators        | 356 ms                                                 | 423 ms: 1.19x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (6): djangocms, telco, unpickle, thrift, regex_effbot, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
