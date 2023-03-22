
# Results vs. 3.11.0

- fork: python
- ref: d1a89ce5156cd4e1eff5
- machine: linux-x86_64
- commit hash: d1a89ce
- commit date: 2023-03-21
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.04x faster                                                   |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                 |
| html5lib       | 64.8 ms                                                | 60.5 ms: 1.07x faster                                                  |
| tornado_http   | 96.5 ms                                                | 91.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| float          | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                  |
| nbody          | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 133 ms: 1.03x faster                                                   |
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.01x faster                                                  |
| regex_effbot   | 3.46 ms                                                | 3.42 ms: 1.01x faster                                                  |
| regex_dna      | 203 ms                                                 | 204 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.59 ms: 1.29x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.08x faster                                                   |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 151 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| unpickle_list        | 4.99 us                                                | 5.05 us: 1.01x slower                                                  |
| pickle_list          | 4.14 us                                                | 4.23 us: 1.02x slower                                                  |
| xml_etree_process    | 53.7 ms                                                | 56.0 ms: 1.04x slower                                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 80.8 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.88 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.56 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.0 ms: 1.07x faster                                                  |
| mako            | 9.83 ms                                                | 10.1 ms: 1.03x slower                                                  |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.7 ms: 2.47x faster                                                  |
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.59 ms: 1.29x faster                                                  |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                   |
| coroutines              | 26.2 ms                                                | 22.2 ms: 1.18x faster                                                  |
| deltablue               | 3.66 ms                                                | 3.17 ms: 1.15x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                   |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.08x faster                                                   |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                 |
| scimark_fft             | 325 ms                                                 | 303 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.28 ms: 1.07x faster                                                  |
| html5lib                | 64.8 ms                                                | 60.5 ms: 1.07x faster                                                  |
| genshi_xml              | 51.4 ms                                                | 48.0 ms: 1.07x faster                                                  |
| logging_simple          | 6.02 us                                                | 5.62 us: 1.07x faster                                                  |
| richards                | 46.1 ms                                                | 43.2 ms: 1.07x faster                                                  |
| spectral_norm           | 98.1 ms                                                | 92.0 ms: 1.07x faster                                                  |
| json                    | 4.87 ms                                                | 4.57 ms: 1.07x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 151 ms: 1.06x faster                                                   |
| coverage                | 99.3 ms                                                | 93.4 ms: 1.06x faster                                                  |
| tornado_http            | 96.5 ms                                                | 91.0 ms: 1.06x faster                                                  |
| nqueens                 | 83.8 ms                                                | 79.7 ms: 1.05x faster                                                  |
| fannkuch                | 384 ms                                                 | 368 ms: 1.05x faster                                                   |
| chaos                   | 68.7 ms                                                | 65.8 ms: 1.04x faster                                                  |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                   |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                   |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                 |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                  |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                                   |
| bench_thread_pool       | 817 us                                                 | 788 us: 1.04x faster                                                   |
| deepcopy                | 341 us                                                 | 330 us: 1.04x faster                                                   |
| 2to3                    | 259 ms                                                 | 251 ms: 1.04x faster                                                   |
| sqlglot_optimize        | 52.7 ms                                                | 50.9 ms: 1.03x faster                                                  |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                                  |
| logging_silent          | 98.0 ns                                                | 94.8 ns: 1.03x faster                                                  |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                   |
| float                   | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                  |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                  |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                 |
| regex_compile           | 136 ms                                                 | 133 ms: 1.03x faster                                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 66.2 ms: 1.03x faster                                                  |
| hexiom                  | 6.34 ms                                                | 6.17 ms: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| nbody                   | 90.0 ms                                                | 87.7 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                  |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 691 ms: 1.02x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                                   |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.02x faster                                                  |
| dulwich_log             | 64.0 ms                                                | 63.0 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                   |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.01x faster                                                  |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                  |
| regex_effbot            | 3.46 ms                                                | 3.42 ms: 1.01x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.9 ms: 1.01x faster                                                  |
| pyflate                 | 419 ms                                                 | 416 ms: 1.01x faster                                                   |
| regex_dna               | 203 ms                                                 | 204 ms: 1.00x slower                                                   |
| gc_traversal            | 3.82 ms                                                | 3.84 ms: 1.00x slower                                                  |
| unpickle_list           | 4.99 us                                                | 5.05 us: 1.01x slower                                                  |
| thrift                  | 760 us                                                 | 771 us: 1.01x slower                                                   |
| pickle_list             | 4.14 us                                                | 4.23 us: 1.02x slower                                                  |
| telco                   | 6.43 ms                                                | 6.60 ms: 1.03x slower                                                  |
| mako                    | 9.83 ms                                                | 10.1 ms: 1.03x slower                                                  |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                  |
| python_startup          | 8.58 ms                                                | 8.88 ms: 1.04x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                  |
| xml_etree_process       | 53.7 ms                                                | 56.0 ms: 1.04x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                  |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| xml_etree_generate      | 75.9 ms                                                | 80.8 ms: 1.06x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.56 ms: 1.09x slower                                                  |
| async_generators        | 356 ms                                                 | 417 ms: 1.17x slower                                                   |
| dask                    | 365 ms                                                 | 501 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (14): async_tree_none, chameleon, sympy_sum, async_tree_io, djangocms, scimark_lu, unpack_sequence, unpickle, async_tree_cpu_io_mixed, async_tree_memoization, mdp, genshi_text, bench_mp_pool, pickle_dict
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230321-3.12.0a6+-d1a89ce/bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce.json: comprehensions
