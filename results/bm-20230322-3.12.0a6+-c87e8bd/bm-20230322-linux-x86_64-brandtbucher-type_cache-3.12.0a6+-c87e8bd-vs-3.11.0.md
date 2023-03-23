
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: c87e8bd
- commit date: 2023-03-22
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| chameleon      | 6.38 ms                                                | 6.64 ms: 1.04x slower                                              |
| docutils       | 2.60 sec                                               | 2.56 sec: 1.01x faster                                             |
| html5lib       | 64.8 ms                                                | 61.9 ms: 1.05x faster                                              |
| tornado_http   | 96.5 ms                                                | 91.7 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                               |
| float          | 76.8 ms                                                | 74.4 ms: 1.03x faster                                              |
| nbody          | 90.0 ms                                                | 90.6 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                               |
| regex_v8       | 22.2 ms                                                | 22.8 ms: 1.02x slower                                              |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                               |
| regex_effbot   | 3.46 ms                                                | 3.57 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.70 ms: 1.27x faster                                              |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                               |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                              |
| pickle_pure_python   | 308 us                                                 | 290 us: 1.06x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 152 ms: 1.06x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| pickle_dict          | 31.2 us                                                | 31.1 us: 1.00x faster                                              |
| pickle_list          | 4.14 us                                                | 4.21 us: 1.02x slower                                              |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| unpickle_list        | 4.99 us                                                | 5.20 us: 1.04x slower                                              |
| xml_etree_process    | 53.7 ms                                                | 57.3 ms: 1.07x slower                                              |
| xml_etree_generate   | 75.9 ms                                                | 81.7 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.88 ms: 1.04x slower                                              |
| python_startup_no_site | 6.04 ms                                                | 6.56 ms: 1.09x slower                                              |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.1 ms: 1.07x faster                                              |
| genshi_text     | 21.5 ms                                                | 21.8 ms: 1.01x slower                                              |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                              |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                              |
| asyncio_tcp             | 883 ms                                                 | 509 ms: 1.73x faster                                               |
| json_dumps              | 12.4 ms                                                | 9.70 ms: 1.27x faster                                              |
| mypy2                   | 420 ms                                                 | 336 ms: 1.25x faster                                               |
| coroutines              | 26.2 ms                                                | 22.5 ms: 1.16x faster                                              |
| unpickle_pure_python    | 227 us                                                 | 203 us: 1.12x faster                                               |
| deltablue               | 3.66 ms                                                | 3.33 ms: 1.10x faster                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.22 ms: 1.09x faster                                              |
| spectral_norm           | 98.1 ms                                                | 90.4 ms: 1.09x faster                                              |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                              |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                               |
| genshi_xml              | 51.4 ms                                                | 48.1 ms: 1.07x faster                                              |
| pickle_pure_python      | 308 us                                                 | 290 us: 1.06x faster                                               |
| scimark_fft             | 325 ms                                                 | 307 ms: 1.06x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 152 ms: 1.06x faster                                               |
| tornado_http            | 96.5 ms                                                | 91.7 ms: 1.05x faster                                              |
| hexiom                  | 6.34 ms                                                | 6.04 ms: 1.05x faster                                              |
| richards                | 46.1 ms                                                | 44.0 ms: 1.05x faster                                              |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                               |
| html5lib                | 64.8 ms                                                | 61.9 ms: 1.05x faster                                              |
| mdp                     | 2.63 sec                                               | 2.51 sec: 1.04x faster                                             |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                               |
| nqueens                 | 83.8 ms                                                | 80.5 ms: 1.04x faster                                              |
| json                    | 4.87 ms                                                | 4.70 ms: 1.04x faster                                              |
| float                   | 76.8 ms                                                | 74.4 ms: 1.03x faster                                              |
| fannkuch                | 384 ms                                                 | 374 ms: 1.03x faster                                               |
| bench_thread_pool       | 817 us                                                 | 794 us: 1.03x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.9 us: 1.03x faster                                              |
| deepcopy                | 341 us                                                 | 333 us: 1.03x faster                                               |
| deepcopy_reduce         | 3.02 us                                                | 2.94 us: 1.03x faster                                              |
| chaos                   | 68.7 ms                                                | 67.0 ms: 1.03x faster                                              |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| sympy_str               | 291 ms                                                 | 284 ms: 1.02x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                             |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                              |
| logging_simple          | 6.02 us                                                | 5.90 us: 1.02x faster                                              |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.02x faster                                              |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.02x faster                                             |
| pprint_safe_repr        | 706 ms                                                 | 693 ms: 1.02x faster                                               |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| docutils                | 2.60 sec                                               | 2.56 sec: 1.01x faster                                             |
| unpack_sequence         | 44.5 ns                                                | 44.0 ns: 1.01x faster                                              |
| sqlglot_optimize        | 52.7 ms                                                | 52.2 ms: 1.01x faster                                              |
| logging_silent          | 98.0 ns                                                | 97.0 ns: 1.01x faster                                              |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                              |
| dulwich_log             | 64.0 ms                                                | 63.4 ms: 1.01x faster                                              |
| crypto_pyaes            | 75.7 ms                                                | 75.3 ms: 1.01x faster                                              |
| pickle_dict             | 31.2 us                                                | 31.1 us: 1.00x faster                                              |
| nbody                   | 90.0 ms                                                | 90.6 ms: 1.01x slower                                              |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                               |
| genshi_text             | 21.5 ms                                                | 21.8 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 746 ms: 1.01x slower                                               |
| pickle_list             | 4.14 us                                                | 4.21 us: 1.02x slower                                              |
| telco                   | 6.43 ms                                                | 6.53 ms: 1.02x slower                                              |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                              |
| regex_v8                | 22.2 ms                                                | 22.8 ms: 1.02x slower                                              |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                               |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                              |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| regex_effbot            | 3.46 ms                                                | 3.57 ms: 1.03x slower                                              |
| python_startup          | 8.58 ms                                                | 8.88 ms: 1.04x slower                                              |
| chameleon               | 6.38 ms                                                | 6.64 ms: 1.04x slower                                              |
| gc_traversal            | 3.82 ms                                                | 3.98 ms: 1.04x slower                                              |
| unpickle_list           | 4.99 us                                                | 5.20 us: 1.04x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.75 ms: 1.06x slower                                              |
| xml_etree_process       | 53.7 ms                                                | 57.3 ms: 1.07x slower                                              |
| async_tree_memoization  | 624 ms                                                 | 667 ms: 1.07x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.46 ms: 1.07x slower                                              |
| thrift                  | 760 us                                                 | 816 us: 1.07x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 81.7 ms: 1.08x slower                                              |
| python_startup_no_site  | 6.04 ms                                                | 6.56 ms: 1.09x slower                                              |
| async_generators        | 356 ms                                                 | 417 ms: 1.17x slower                                               |
| dask                    | 365 ms                                                 | 509 ms: 1.39x slower                                               |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (11): pyflate, scimark_monte_carlo, logging_format, bench_mp_pool, sqlglot_normalize, sympy_sum, scimark_lu, async_tree_none, async_tree_io, raytrace, unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-c87e8bd/bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd.json: comprehensions
