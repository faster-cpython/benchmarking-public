
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: 212046c
- commit date: 2023-03-23
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| chameleon      | 6.38 ms                                                | 6.48 ms: 1.02x slower                                                    |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                   |
| html5lib       | 64.8 ms                                                | 61.6 ms: 1.05x faster                                                    |
| tornado_http   | 96.5 ms                                                | 92.5 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.1 ms: 1.05x faster                                                    |
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                                     |
| nbody          | 90.0 ms                                                | 87.8 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                                     |
| regex_v8       | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                    |
| regex_effbot   | 3.46 ms                                                | 3.37 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.56 ms: 1.29x faster                                                    |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.13x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.09x faster                                                     |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                                    |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 99.2 ms: 1.05x faster                                                    |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                                    |
| pickle_list          | 4.14 us                                                | 4.27 us: 1.03x slower                                                    |
| xml_etree_process    | 53.7 ms                                                | 56.0 ms: 1.04x slower                                                    |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                                    |
| unpickle_list        | 4.99 us                                                | 5.25 us: 1.05x slower                                                    |
| xml_etree_generate   | 75.9 ms                                                | 80.9 ms: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.82 ms: 1.03x slower                                                    |
| python_startup_no_site | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.4 ms: 1.06x faster                                                    |
| django_template | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                    |
| mako            | 9.83 ms                                                | 10.1 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                    |
| asyncio_tcp             | 883 ms                                                 | 510 ms: 1.73x faster                                                     |
| json_dumps              | 12.4 ms                                                | 9.56 ms: 1.29x faster                                                    |
| mypy2                   | 420 ms                                                 | 335 ms: 1.25x faster                                                     |
| coroutines              | 26.2 ms                                                | 22.6 ms: 1.16x faster                                                    |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.13x faster                                                     |
| deltablue               | 3.66 ms                                                | 3.27 ms: 1.12x faster                                                    |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.09x faster                                                     |
| gc_traversal            | 3.82 ms                                                | 3.53 ms: 1.08x faster                                                    |
| spectral_norm           | 98.1 ms                                                | 90.9 ms: 1.08x faster                                                    |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                                    |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                   |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                                     |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.29 ms: 1.07x faster                                                    |
| unpack_sequence         | 44.5 ns                                                | 41.7 ns: 1.07x faster                                                    |
| genshi_xml              | 51.4 ms                                                | 48.4 ms: 1.06x faster                                                    |
| nqueens                 | 83.8 ms                                                | 79.4 ms: 1.06x faster                                                    |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                     |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.05x faster                                                     |
| html5lib                | 64.8 ms                                                | 61.6 ms: 1.05x faster                                                    |
| float                   | 76.8 ms                                                | 73.1 ms: 1.05x faster                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 99.2 ms: 1.05x faster                                                    |
| mdp                     | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                   |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                                     |
| richards                | 46.1 ms                                                | 44.1 ms: 1.05x faster                                                    |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                     |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                    |
| tornado_http            | 96.5 ms                                                | 92.5 ms: 1.04x faster                                                    |
| hexiom                  | 6.34 ms                                                | 6.08 ms: 1.04x faster                                                    |
| fannkuch                | 384 ms                                                 | 370 ms: 1.04x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                   |
| json                    | 4.87 ms                                                | 4.70 ms: 1.04x faster                                                    |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                     |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                                    |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                                     |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                                     |
| chaos                   | 68.7 ms                                                | 66.6 ms: 1.03x faster                                                    |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                                     |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                   |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                    |
| bench_thread_pool       | 817 us                                                 | 794 us: 1.03x faster                                                     |
| regex_v8                | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                    |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                    |
| sympy_str               | 291 ms                                                 | 284 ms: 1.03x faster                                                     |
| crypto_pyaes            | 75.7 ms                                                | 73.8 ms: 1.03x faster                                                    |
| regex_effbot            | 3.46 ms                                                | 3.37 ms: 1.03x faster                                                    |
| nbody                   | 90.0 ms                                                | 87.8 ms: 1.02x faster                                                    |
| coverage                | 99.3 ms                                                | 97.0 ms: 1.02x faster                                                    |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                    |
| logging_simple          | 6.02 us                                                | 5.91 us: 1.02x faster                                                    |
| sqlglot_optimize        | 52.7 ms                                                | 51.8 ms: 1.02x faster                                                    |
| scimark_monte_carlo     | 68.0 ms                                                | 67.0 ms: 1.01x faster                                                    |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                                    |
| raytrace                | 291 ms                                                 | 288 ms: 1.01x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.01x faster                                                     |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                    |
| deepcopy_reduce         | 3.02 us                                                | 3.00 us: 1.01x faster                                                    |
| logging_silent          | 98.0 ns                                                | 97.5 ns: 1.01x faster                                                    |
| dulwich_log             | 64.0 ms                                                | 63.8 ms: 1.00x faster                                                    |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                   |
| chameleon               | 6.38 ms                                                | 6.48 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 749 ms: 1.02x slower                                                     |
| django_template         | 32.3 ms                                                | 33.0 ms: 1.02x slower                                                    |
| mako                    | 9.83 ms                                                | 10.1 ms: 1.03x slower                                                    |
| python_startup          | 8.58 ms                                                | 8.82 ms: 1.03x slower                                                    |
| pickle_list             | 4.14 us                                                | 4.27 us: 1.03x slower                                                    |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                     |
| xml_etree_process       | 53.7 ms                                                | 56.0 ms: 1.04x slower                                                    |
| thrift                  | 760 us                                                 | 792 us: 1.04x slower                                                     |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                    |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                                    |
| unpickle_list           | 4.99 us                                                | 5.25 us: 1.05x slower                                                    |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.06x slower                                                    |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.06x slower                                                    |
| xml_etree_generate      | 75.9 ms                                                | 80.9 ms: 1.07x slower                                                    |
| async_tree_memoization  | 624 ms                                                 | 673 ms: 1.08x slower                                                     |
| python_startup_no_site  | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                    |
| async_generators        | 356 ms                                                 | 416 ms: 1.17x slower                                                     |
| dask                    | 365 ms                                                 | 512 ms: 1.40x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (11): djangocms, async_tree_none, logging_format, meteor_contest, regex_dna, pyflate, bench_mp_pool, sympy_sum, genshi_text, telco, unpickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-212046c/bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c.json: comprehensions
