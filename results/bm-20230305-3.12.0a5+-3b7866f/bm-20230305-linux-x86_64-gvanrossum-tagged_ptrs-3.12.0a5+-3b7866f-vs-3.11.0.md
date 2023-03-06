
# Results vs. 3.11.0

- fork: gvanrossum
- ref: tagged_ptrs
- machine: linux-x86_64
- commit hash: 3b7866f
- commit date: 2023-03-05
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.02x faster                                              |
| chameleon      | 6.38 ms                                                | 6.64 ms: 1.04x slower                                             |
| docutils       | 2.60 sec                                               | 2.59 sec: 1.00x faster                                            |
| html5lib       | 64.8 ms                                                | 63.2 ms: 1.03x faster                                             |
| tornado_http   | 96.5 ms                                                | 96.0 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                              |
| float          | 76.8 ms                                                | 76.0 ms: 1.01x faster                                             |
| nbody          | 90.0 ms                                                | 101 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.36 ms: 1.03x faster                                             |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                             |
| regex_compile  | 136 ms                                                 | 138 ms: 1.01x slower                                              |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.58 ms: 1.29x faster                                             |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                             |
| unpickle_pure_python | 227 us                                                 | 208 us: 1.09x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                              |
| pickle_pure_python   | 308 us                                                 | 297 us: 1.04x faster                                              |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                              |
| pickle_dict          | 31.2 us                                                | 31.3 us: 1.01x slower                                             |
| pickle_list          | 4.14 us                                                | 4.24 us: 1.02x slower                                             |
| unpickle_list        | 4.99 us                                                | 5.11 us: 1.03x slower                                             |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                             |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                             |
| xml_etree_process    | 53.7 ms                                                | 57.4 ms: 1.07x slower                                             |
| xml_etree_generate   | 75.9 ms                                                | 83.1 ms: 1.09x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.02 ms: 1.05x slower                                             |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.7 ms: 1.04x faster                                             |
| genshi_text     | 21.5 ms                                                | 22.0 ms: 1.02x slower                                             |
| django_template | 32.3 ms                                                | 34.3 ms: 1.06x slower                                             |
| mako            | 9.83 ms                                                | 10.5 ms: 1.07x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.3 ms: 2.34x faster                                             |
| asyncio_tcp             | 883 ms                                                 | 505 ms: 1.75x faster                                              |
| json_dumps              | 12.4 ms                                                | 9.58 ms: 1.29x faster                                             |
| mypy2                   | 420 ms                                                 | 340 ms: 1.24x faster                                              |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                             |
| deltablue               | 3.66 ms                                                | 3.34 ms: 1.09x faster                                             |
| unpickle_pure_python    | 227 us                                                 | 208 us: 1.09x faster                                              |
| coroutines              | 26.2 ms                                                | 24.0 ms: 1.09x faster                                             |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                              |
| json                    | 4.87 ms                                                | 4.56 ms: 1.07x faster                                             |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                            |
| richards                | 46.1 ms                                                | 44.3 ms: 1.04x faster                                             |
| pickle_pure_python      | 308 us                                                 | 297 us: 1.04x faster                                              |
| genshi_xml              | 51.4 ms                                                | 49.7 ms: 1.04x faster                                             |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                             |
| regex_effbot            | 3.46 ms                                                | 3.36 ms: 1.03x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                              |
| aiohttp                 | 1.05 ms                                                | 1.02 ms: 1.03x faster                                             |
| html5lib                | 64.8 ms                                                | 63.2 ms: 1.03x faster                                             |
| coverage                | 99.3 ms                                                | 97.0 ms: 1.02x faster                                             |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                              |
| sympy_expand            | 475 ms                                                 | 467 ms: 1.02x faster                                              |
| logging_simple          | 6.02 us                                                | 5.92 us: 1.02x faster                                             |
| 2to3                    | 259 ms                                                 | 255 ms: 1.02x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.02x faster                                             |
| bench_thread_pool       | 817 us                                                 | 808 us: 1.01x faster                                              |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                             |
| float                   | 76.8 ms                                                | 76.0 ms: 1.01x faster                                             |
| tornado_http            | 96.5 ms                                                | 96.0 ms: 1.01x faster                                             |
| pprint_pformat          | 1.46 sec                                               | 1.45 sec: 1.00x faster                                            |
| docutils                | 2.60 sec                                               | 2.59 sec: 1.00x faster                                            |
| sqlglot_optimize        | 52.7 ms                                                | 52.6 ms: 1.00x faster                                             |
| dulwich_log             | 64.0 ms                                                | 64.3 ms: 1.01x slower                                             |
| pprint_safe_repr        | 706 ms                                                 | 710 ms: 1.01x slower                                              |
| pickle_dict             | 31.2 us                                                | 31.3 us: 1.01x slower                                             |
| unpack_sequence         | 44.5 ns                                                | 44.8 ns: 1.01x slower                                             |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                            |
| sqlalchemy_declarative  | 138 ms                                                 | 140 ms: 1.01x slower                                              |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                             |
| regex_compile           | 136 ms                                                 | 138 ms: 1.01x slower                                              |
| mdp                     | 2.63 sec                                               | 2.66 sec: 1.01x slower                                            |
| sqlalchemy_imperative   | 18.1 ms                                                | 18.3 ms: 1.01x slower                                             |
| deepcopy                | 341 us                                                 | 346 us: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 750 ms: 1.02x slower                                              |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                              |
| genshi_text             | 21.5 ms                                                | 22.0 ms: 1.02x slower                                             |
| sympy_sum               | 166 ms                                                 | 169 ms: 1.02x slower                                              |
| pickle_list             | 4.14 us                                                | 4.24 us: 1.02x slower                                             |
| hexiom                  | 6.34 ms                                                | 6.49 ms: 1.02x slower                                             |
| telco                   | 6.43 ms                                                | 6.59 ms: 1.02x slower                                             |
| unpickle_list           | 4.99 us                                                | 5.11 us: 1.03x slower                                             |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                             |
| raytrace                | 291 ms                                                 | 299 ms: 1.03x slower                                              |
| deepcopy_memo           | 35.8 us                                                | 36.8 us: 1.03x slower                                             |
| chaos                   | 68.7 ms                                                | 70.7 ms: 1.03x slower                                             |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                             |
| thrift                  | 760 us                                                 | 783 us: 1.03x slower                                              |
| deepcopy_reduce         | 3.02 us                                                | 3.12 us: 1.03x slower                                             |
| nqueens                 | 83.8 ms                                                | 86.7 ms: 1.04x slower                                             |
| scimark_fft             | 325 ms                                                 | 337 ms: 1.04x slower                                              |
| spectral_norm           | 98.1 ms                                                | 102 ms: 1.04x slower                                              |
| chameleon               | 6.38 ms                                                | 6.64 ms: 1.04x slower                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 70.9 ms: 1.04x slower                                             |
| python_startup          | 8.58 ms                                                | 9.02 ms: 1.05x slower                                             |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                             |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.86 ms: 1.06x slower                                             |
| django_template         | 32.3 ms                                                | 34.3 ms: 1.06x slower                                             |
| scimark_lu              | 108 ms                                                 | 115 ms: 1.06x slower                                              |
| gc_traversal            | 3.82 ms                                                | 4.07 ms: 1.07x slower                                             |
| mako                    | 9.83 ms                                                | 10.5 ms: 1.07x slower                                             |
| xml_etree_process       | 53.7 ms                                                | 57.4 ms: 1.07x slower                                             |
| async_tree_memoization  | 624 ms                                                 | 670 ms: 1.07x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.78 ms: 1.08x slower                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                             |
| sqlglot_parse           | 1.36 ms                                                | 1.48 ms: 1.09x slower                                             |
| xml_etree_generate      | 75.9 ms                                                | 83.1 ms: 1.09x slower                                             |
| nbody                   | 90.0 ms                                                | 101 ms: 1.12x slower                                              |
| async_generators        | 356 ms                                                 | 423 ms: 1.19x slower                                              |
| dask                    | 365 ms                                                 | 517 ms: 1.42x slower                                              |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (14): go, sympy_integrate, logging_format, sympy_str, scimark_sor, bench_mp_pool, sqlglot_normalize, fannkuch, crypto_pyaes, meteor_contest, pyflate, async_tree_none, logging_silent, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230305-3.12.0a5+-3b7866f/bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f.json: comprehensions
