
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: bde6bec
- commit date: 2023-03-23
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                     |
| chameleon      | 6.38 ms                                                | 6.55 ms: 1.03x slower                                                    |
| docutils       | 2.60 sec                                               | 2.56 sec: 1.01x faster                                                   |
| html5lib       | 64.8 ms                                                | 62.2 ms: 1.04x faster                                                    |
| tornado_http   | 96.5 ms                                                | 92.7 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                                     |
| float          | 76.8 ms                                                | 74.0 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                                     |
| regex_v8       | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                    |
| regex_effbot   | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.53 ms: 1.30x faster                                                    |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                     |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                    |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                     |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                    |
| pickle_list          | 4.14 us                                                | 4.24 us: 1.02x slower                                                    |
| pickle_dict          | 31.2 us                                                | 31.9 us: 1.02x slower                                                    |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                                    |
| xml_etree_process    | 53.7 ms                                                | 56.5 ms: 1.05x slower                                                    |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                                    |
| xml_etree_generate   | 75.9 ms                                                | 81.9 ms: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.83 ms: 1.03x slower                                                    |
| python_startup_no_site | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                    |
| mako            | 9.83 ms                                                | 9.96 ms: 1.01x slower                                                    |
| genshi_text     | 21.5 ms                                                | 22.2 ms: 1.03x slower                                                    |
| django_template | 32.3 ms                                                | 33.8 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.7 ms: 2.47x faster                                                    |
| asyncio_tcp             | 883 ms                                                 | 509 ms: 1.74x faster                                                     |
| json_dumps              | 12.4 ms                                                | 9.53 ms: 1.30x faster                                                    |
| mypy2                   | 420 ms                                                 | 337 ms: 1.24x faster                                                     |
| coroutines              | 26.2 ms                                                | 23.0 ms: 1.14x faster                                                    |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                                     |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                     |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.24 ms: 1.08x faster                                                    |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                    |
| gc_traversal            | 3.82 ms                                                | 3.54 ms: 1.08x faster                                                    |
| deltablue               | 3.66 ms                                                | 3.40 ms: 1.07x faster                                                    |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 41.6 ns: 1.07x faster                                                    |
| genshi_xml              | 51.4 ms                                                | 48.2 ms: 1.07x faster                                                    |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.05x faster                                                     |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                                     |
| richards                | 46.1 ms                                                | 44.1 ms: 1.05x faster                                                    |
| html5lib                | 64.8 ms                                                | 62.2 ms: 1.04x faster                                                    |
| json                    | 4.87 ms                                                | 4.67 ms: 1.04x faster                                                    |
| tornado_http            | 96.5 ms                                                | 92.7 ms: 1.04x faster                                                    |
| spectral_norm           | 98.1 ms                                                | 94.3 ms: 1.04x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                     |
| float                   | 76.8 ms                                                | 74.0 ms: 1.04x faster                                                    |
| mdp                     | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                   |
| deepcopy                | 341 us                                                 | 330 us: 1.04x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                   |
| logging_simple          | 6.02 us                                                | 5.83 us: 1.03x faster                                                    |
| hexiom                  | 6.34 ms                                                | 6.14 ms: 1.03x faster                                                    |
| coverage                | 99.3 ms                                                | 96.3 ms: 1.03x faster                                                    |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                     |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                     |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                                    |
| bench_thread_pool       | 817 us                                                 | 796 us: 1.03x faster                                                     |
| scimark_fft             | 325 ms                                                 | 317 ms: 1.03x faster                                                     |
| pprint_safe_repr        | 706 ms                                                 | 690 ms: 1.02x faster                                                     |
| nqueens                 | 83.8 ms                                                | 81.9 ms: 1.02x faster                                                    |
| sympy_str               | 291 ms                                                 | 285 ms: 1.02x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                                    |
| sympy_expand            | 475 ms                                                 | 467 ms: 1.02x faster                                                     |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                    |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                                     |
| pycparser               | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                   |
| docutils                | 2.60 sec                                               | 2.56 sec: 1.01x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.01x faster                                                    |
| chaos                   | 68.7 ms                                                | 67.7 ms: 1.01x faster                                                    |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                     |
| fannkuch                | 384 ms                                                 | 379 ms: 1.01x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 52.0 ms: 1.01x faster                                                    |
| logging_format          | 6.48 us                                                | 6.40 us: 1.01x faster                                                    |
| crypto_pyaes            | 75.7 ms                                                | 75.1 ms: 1.01x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.00x faster                                                     |
| sympy_sum               | 166 ms                                                 | 166 ms: 1.00x slower                                                     |
| logging_silent          | 98.0 ns                                                | 98.4 ns: 1.00x slower                                                    |
| telco                   | 6.43 ms                                                | 6.48 ms: 1.01x slower                                                    |
| regex_v8                | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                    |
| mako                    | 9.83 ms                                                | 9.96 ms: 1.01x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 736 ms                                                 | 748 ms: 1.02x slower                                                     |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                    |
| pickle_list             | 4.14 us                                                | 4.24 us: 1.02x slower                                                    |
| pickle_dict             | 31.2 us                                                | 31.9 us: 1.02x slower                                                    |
| chameleon               | 6.38 ms                                                | 6.55 ms: 1.03x slower                                                    |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                     |
| genshi_text             | 21.5 ms                                                | 22.2 ms: 1.03x slower                                                    |
| python_startup          | 8.58 ms                                                | 8.83 ms: 1.03x slower                                                    |
| regex_effbot            | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                    |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                                    |
| django_template         | 32.3 ms                                                | 33.8 ms: 1.05x slower                                                    |
| xml_etree_process       | 53.7 ms                                                | 56.5 ms: 1.05x slower                                                    |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.05x slower                                                    |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                                    |
| thrift                  | 760 us                                                 | 806 us: 1.06x slower                                                     |
| sqlglot_transpile       | 1.65 ms                                                | 1.76 ms: 1.07x slower                                                    |
| async_tree_memoization  | 624 ms                                                 | 673 ms: 1.08x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.47 ms: 1.08x slower                                                    |
| xml_etree_generate      | 75.9 ms                                                | 81.9 ms: 1.08x slower                                                    |
| python_startup_no_site  | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                    |
| async_generators        | 356 ms                                                 | 411 ms: 1.16x slower                                                     |
| dask                    | 365 ms                                                 | 512 ms: 1.40x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (10): scimark_monte_carlo, djangocms, meteor_contest, bench_mp_pool, deepcopy_reduce, pyflate, dulwich_log, nbody, regex_dna, async_tree_none
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-bde6bec/bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec.json: comprehensions
